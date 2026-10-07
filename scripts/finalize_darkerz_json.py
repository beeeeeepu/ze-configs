import json
import math
import sys
from pathlib import Path
sys.path.insert(0, 'scripts')
import convert_cs2fixes_to_darkerz as old
root = Path('cs2-configs/entwatch/darkerz')
allowed = {'default','darkred','purple','green','lightgreen','lime','red','grey','team','red2','olive','a','lightblue','blue','d','pink','darkorange','orange','darkblue','gold','white','yellow','magenta','silver','bluegrey','lightred','cyan','gray','lightyellow'}
color_map = {'heal':'green','fullred':'red','agreen':'green','agrey':'grey','dakred':'darkred','gravity':'purple','4698':'white'}
report=[]
for source in sorted(old.SOURCE.glob('*.jsonc')):
    if source.name == 'template.jsonc':
        continue
    items=old.parse_jsonc(source.read_text(encoding='utf-8-sig'))
    notes=[]
    out=[]
    for item in items:
        x=old.convert_item(item,notes)
        color=x['Color'].strip('{}')
        if color not in allowed:
            replacement=color_map.get(color,'white')
            notes.append(f"{item.get('name')}: color {color} replaced by {replacement}")
            x['Color']='{'+replacement+'}'
        for ability in x['AbilityList']:
            cd=ability['CoolDown']
            if isinstance(cd,float) and not cd.is_integer():
                ability['CoolDown']=math.ceil(cd)
                notes.append(f"{item.get('name')}: cooldown {cd} rounded up to {ability['CoolDown']}")
            elif isinstance(cd,float):
                ability['CoolDown']=int(cd)
            if ability['Mode']==4 and ability['CoolDown']==0:
                ability['Mode']=3
            if not ability['ButtonClass']:
                notes.append(f"{item.get('name')}: ability {ability['ButtonID']} has no supported button class")
        out.append(x)
    target=root/(source.stem+'.json')
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if notes:
        report.append(source.name+': '+ '; '.join(dict.fromkeys(notes)))
for stale in root.glob('*.jsonc'):
    stale.unlink()
(root/'CONVERSION_REVIEW.txt').write_text('MS-EntWatch cannot exactly reproduce some CS2Fixes handlers. Inspect these maps in game.\n\n'+'\n'.join(report)+'\n',encoding='utf-8')
print(f'Converted {len(list(root.glob("*.json")))} JSON files; {len(report)} maps have behavior notes')
