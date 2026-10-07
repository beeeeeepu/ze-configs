"""Convert CS2Fixes EntWatch JSONC files to DarkerZ EntWatch JSONC."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'cs2-configs' / 'entwatch'
SOURCE = ROOT / 'cs2fixes'
TARGET = ROOT / 'darkerz'


def parse_jsonc(text):
    # Comments and trailing commas occur in the source files.
    text = re.sub(r'("(?:\\.|[^"\\])*")|//[^\n]*|/\*.*?\*/',
                  lambda m: m.group(1) if m.group(1) else '', text,
                  flags=re.S).replace('\r', '')
    return json.loads(re.sub(r',\s*([}\]])', r'\1', text))


def convert_item(item, notes):
    result = {
        'Name': item.get('name', ''),
        'ShortName': item.get('shortname', item.get('name', '')),
        'Color': '{' + item.get('color', 'default').strip('{}') + '}',
        'HammerID': str(item.get('hammerid', '')),
        'AllowTransfer': item.get('transfer', True),
        'Chat': item.get('message', True),
        'Hud': item.get('ui', True),
    }
    triggers = item.get('triggers') or []
    if triggers:
        result['TriggerID'] = str(triggers[0])
        if len(triggers) > 1:
            notes.append('Multiple triggers: only first TriggerID can be represented')
    handlers = item.get('handlers') or []
    buttons = [h for h in handlers if h.get('type') == 'button']
    tracked = [h for h in handlers if h.get('type') != 'button' and h.get('event') == 'OnPass']
    abilities = []
    for handler in handlers:
        if handler.get('type') != 'button' and handler.get('event') == 'OnPass':
            continue
        mode = handler.get('mode', 0)
        if handler.get('type') == 'counterdown':
            new_mode = 6
        elif handler.get('type') == 'counterup':
            new_mode = 7
        else:
            new_mode = {0: 0, 1: 1, 2: 2, 3: 4, 4: 5}.get(mode, 0)
        companion = tracked.pop(0) if handler in buttons and tracked else None
        setting = companion or handler
        if companion:
            m = companion.get('mode', 0)
            new_mode = {0: 0, 1: 1, 2: 2, 3: 4, 4: 5}.get(m, 0)
            notes.append('OnPass handler ' + str(companion.get('hammerid', '')) + ' used for cooldown; verify button behavior')
        ability = {
            'ButtonID': str(handler.get('hammerid', '')),
            'ButtonClass': 'func_button' if handler.get('type') == 'button' else '',
            'Chat_Uses': setting.get('message', True),
            'Mode': new_mode,
            'MaxUses': setting.get('maxuses', 0),
            'CoolDown': setting.get('cooldown', 0),
            'Ignore': not setting.get('ui', True),
        }
        if handler.get('name'):
            ability['Name'] = handler['name']
        if new_mode in (6, 7):
            ability['MathID'] = str(handler.get('hammerid', ''))
        if handler.get('event') not in (None, 'OnPressed', 'OutValue'):
            notes.append('Unsupported event ' + str(handler['event']) + ' on ' + ability['ButtonID'])
        if handler.get('offset') not in (None, [0, 0]):
            notes.append('Unsupported counter offset on ' + ability['ButtonID'])
        abilities.append(ability)
    for handler in tracked:
        notes.append('Unpaired OnPass handler ' + str(handler.get('hammerid', '')))
    result['AbilityList'] = abilities
    return result


def main():
    TARGET.mkdir(exist_ok=True)
    errors = []
    converted = 0
    for path in sorted(SOURCE.glob('*.jsonc')):
        if path.name == 'template.jsonc':
            continue
        try:
            data = parse_jsonc(path.read_text(encoding='utf-8-sig'))
            if not isinstance(data, list):
                raise ValueError('root is not an array')
            notes = []
            output = [convert_item(item, notes) for item in data]
            content = json.dumps(output, ensure_ascii=False, indent=2)
            if notes:
                content = '// REVIEW: ' + '; '.join(dict.fromkeys(notes)) + '\n' + content
            (TARGET / path.name).write_text(content + '\n', encoding='utf-8')
            converted += 1
        except Exception as exc:
            errors.append(f'{path.name}: {exc}')
    print(f'Converted {converted} files; {len(errors)} errors')
    for error in errors:
        print(error)


if __name__ == '__main__':
    main()
    import finalize_darkerz_json  # emit strict JSON after conversion
