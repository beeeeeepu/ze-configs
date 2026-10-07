
# CS2 Config Formatting

> [!CAUTION]
> Config options vary from server to server due to different plugins. I will separate configs for each server and include information on differences. Do keep this in mind when you want to look at configs I have made.

**Table of Contents:**
1. [CS2Fixes](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#cs2fixes)
    - [EntWatch](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#entwatch)
    - [BossHUD](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#bosshud)
    - [AdminRoom](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#adminroom)
2. [ExG](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#exg)
    - [EntWatch](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#entwatch-1)
    - [BossHUD](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#bosshud-1)
3. [FyS](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#fys)
    - [EntWatch](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#entwatch-2)
    - [BossHUD](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#bosshud-2)
4. [ZombieDen](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#zombieden)
    - [EntWatch](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#entwatch-3)
    - [BossHUD](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#bosshud-3)
4. [DarkerZ](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#darkerz)
    - [EntWatchSharp/MS-EntWatch](https://github.com/notkoen/ze-configs/blob/main/info/cs2.md#entwatch-2)

## CS2Fixes

### EntWatch

This version of EntWatch is publicly available [here](https://github.com/Source2ZE/CS2Fixes).

Find entity classnames that start with `weapon_` as a starting point for creating EntWatch configs. For each item you're going to want a new block in the root array. The format is available below. EntWatch also supports filtering triggering from restricted players without a weapon.

List of available colors:
- white, default
- darkred
- team
- green
- lightgreen
- olive
- red
- gray, grey
- yellow
- silver
- blue
- darkblue
- purple, pink
- red2
- orange, gold

```jsonc
[
  {
    "name": "Item Name",            // (string)     -> Name of item that appears in chat
    "shortname": "Short Name",      // (string)     -> Name of item that appears on the HUD
    "hammerid": "",                 // (string)     -> Hammerid of the weapon entity
    "message": true,                // (bool)       -> Whether to show pickup/drop messages in chat
    "ui": true,                     // (bool)       -> Whether to show this item on the HUD
    "transfer": true,               // (bool)       -> Whether this item can be transferred (knife items default to false)
    "color": "",                    // (string)     -> Item color for chat messages, hud, and glow (see list of colors)
    "triggers": [""],               // (string[]?)  -> Array of trigger hammerids associated with the item
    "templated": true,              // (bool)       -> Whether the entity of this handler is templated with the item weapon, (auto detected if not specified)
    "handlers": [
      {
        "name": "Handler",          // (string?)    -> Extra name to show in chat when used e.g. XXX has used Item Name (Handler)
        "type": "button",           // (string)     -> Ability type: 'button', 'counterdown', 'counterdown', or leave empty for output tracking
        "hammerid": "",             // (string)     -> Hammerid of the ability
        "event": "OnPressed",       // (string)     -> Output name (for output type)
        "mode": 2,                  // (int)        -> Mode of the handler
                                    //                  0/1 = None
                                    //                  2 = Cooldown,           3 = MaxUses (cooldown between each)
                                    //                  4 = CooldownAfterUses,  5 = CounterValue
        "offset": [0,0],            // (int[]?)     -> Add specified offset to counter values [counter value, counter max]
        "cooldown": 0,              // (int)        -> Cooldown duration (Mode 2/3/4 only)
        "maxuses": 0,               // (int)        -> Maxuses (Mode 3/4 only)
        "message": true,            // (bool)       -> Whether to show when this is used in chat
        "ui": true,                 // (bool)       -> Whether to track this handler on the HUD
        "templated": true           // (bool?)      -> Whether handler is templated with the item (auto detected if not specified)
      }
    ]
  }
]
```

<details>
    <summary>Clean Template</summary>

```jsonc
[
  // Full Config
  {
    "name": "",
    "shortname": "",
    "hammerid": "",
    "message": true,
    "ui": true,
    "transfer": true,
    "color": "",
    "triggers": [""],
    "templated": true,
    "handlers": [
      {
        "name": "Handler",
        "type": "button",
        "hammerid": "",
        "event": "OnPressed",
        "mode": 0,
        "cooldown": 0,
        "maxuses": 0,
        "offset": [0,0],
        "message": true,
        "ui": true,
        "templated": true
      }
    ]
  },
  // Regular button
  {
    "name": "",
    "shortname": "",
    "hammerid": "",
    "message": true,
    "ui": true,
    "transfer": true,
    "color": "",
    "triggers": [""],
    "handlers": [
      {
        "type": "button",
        "hammerid": "",
        "event": "OnPressed",
        "mode": 0,
        "cooldown": 0,
        "maxuses": 0,
        "message": true,
        "ui": true
      }
    ]
  },
  // Button and filter separate (most reliable)
  {
    "name": "",
    "shortname": "",
    "hammerid": "",
    "message": true,
    "ui": true,
    "transfer": true,
    "color": "",
    "triggers": [""],
    "handlers": [
      {
        "type": "button",
        "hammerid": ""
      },
      {
        "hammerid": "",
        "event": "OnPass",
        "mode": 0,
        "cooldown": 0,
        "maxuses": 0,
        "message": true,
        "ui": true
      }
    ]
  },
]
```
</details>

### BossHUD

> [!CAUTION]
> CS2Fixes BossHUD is still in active development and thus not yet released publicly, so config formatting **SHOULD NOT** be considered final.

Find entity classnames that are either `math_counter`, `func_breakable`, or `func_physbox` as a starting point for creating BossHUD configs. For each boss and NPC, you're going to want a new block in the root array. The format is available below. You can specify entities with either its targetname or its hammerid by starting the string with `#` (e.g. "#123456").

```jsonc
[
  {
    "name": "",                 // (string?)  -> Name of boss that appears in hud
    "breakable": "",            // (string)   -> Targetname/hammerid of breakable
    "counter": "",              // (string)   -> Targetname/hammerid of main counter
    "iterator": "",             // (string?)  -> Targetname/hammerid of iterator counter
    "backup": "",               // (string?)  -> Targetname/hammerid of backup counter

    "trigger":                  // Boss trigger event (optional)
    {
      "ent": "",                // (string)   -> Targetname/hammerid of entity
      "output": "",             // (string)   -> Entity output
      "delay": 0.0              // (float?)   -> Delay after output that triggers the boss
    },

    "showtrigger":              // Display boss health event (optional)
    {
      "ent": "",                // (string)   -> Targetname/hammerid of entity
      "output": "",             // (string)   -> Entity output
      "delay": 0.0              // (float?)   -> Delay after event that shows boss health
    },

    "killtrigger":              // Boss death event (optional)
    {
      "ent": "",                // (string)   -> Targetname/hammerid of entity
      "output": "",             // (string)   -> Entity output
      "delay": 0.0              // (float?)   -> Delay after event that kills the boss
    },

    "hurttrigger":              // Boss damage event (optional)
    {
      "ent": "",                // (string)   -> Targetname/hammerid of entity
      "output": ""              // (string)   -> Entity output
    },

    "reversecounter": false,    // (bool?)    -> Whether main counter has OnHitMax outputs
    "reverseiterator": false,   // (bool?)    -> Whether iterator counter has OnHitMax outputs
    "hitmarkeronly": false,     // (bool?)    -> Whether only hitmarkers should be shown when hitting boss
    "minorhud": false,          // (bool?)    -> Whether boss should should be displayed as no-bar hud variant
    "multitrigger": false,      // (bool?)    -> Whether boss can be triggered multiple times (multiple instances)
    "templated": false,         // (bool?)    -> Whether boss is templated and has name fixup
    "showbeaten": true,         // (bool?)    -> Whether top boss damage should be displayed after boss death
    "timeout": 0.0,             // (float?)   -> Specify time before boss health is hidden after taking no damage
    "offset": 0.0,              // (float?)   -> Specify amount of health to ADD to displayed health (negative to subtract)
    "offsetiterator": 0.0,      // (float?)   -> Specify amount of iterator segments to ADD to displayed health (negative to subtract)
    "maxhp": 0.0                // (float?)   -> If the boss has more than this HP, it will not start showing on the HUD (0.0 = no limit)
  }
]
```

<details>
    <summary>Clean Template</summary>

```jsonc
[
  // Full config
  {
    "name": "",
    "breakable": "",
    "counter": "",
    "iterator": "",
    "backup": "",
    "trigger": { "ent": "", "output": "", "delay": 0.0 },
    "showtrigger": { "ent": "", "output": "", "delay": 0.0 },
    "killtrigger": { "ent": "", "output": "", "delay": 0.0 },
    "hurttrigger": { "ent": "", "output": "" },
    "reversecounter": false,
    "reverseiterator": false,
    "hitmarkeronly": false,
    "minorhud": false,
    "multitrigger": false,
    "templated": false,
    "showbeaten": true,
    "timeout": 0.0,
    "offset": 0.0,
    "offsetiterator": 0.0,
    "maxhp": 0.0
  },

  // Breakable type boss
  {
    "name": "",
    "breakable": ""
  },

  // Counter type boss
  {
    "name": "",
    "counter": ""
  },

  // Counter, backup, and iterator type boss
  {
    "name": "",
    "counter": "",
    "backup": "",
    "iterator": ""
  },

  // Counter and iterator type boss
  {
    "name": "",
    "counter": "",
    "iterator": ""
  },

  // Breakable and iterator type boss
  {
    "name": "",
    "breakable": "",
    "iterator": ""
  },

  // NPC display (show health)
  {
    "name": "",
    "minorhud": true,
    "multitrigger": true,
    "showbeaten": false,
    "templated": true,
    "timeout": 1.0,
    "breakable": ""
  },
  
  // NPC hitmarkers only
  {
    "hitmarkeronly": true,
    "multitrigger": true,
    "showbeaten": false,
    "templated": true,
    "breakable": ""
  }
]
```
</details>

### AdminRoom

The AdminRoom feature is exclusive to GFL's version of CS2Fixes. All admin room coordindates are stored in one single [file](https://github.com/notkoen/ze-configs/blob/main/cs2-configs/adminroom.jsonc). Coordinates are stored with map names as the key, and coordinates as an array.

## EXG

### EntWatch

```jsonc
[
  {
    "Name": "",                 // Name of item that appears in chat
    "ShortName": "",            // Name of item that appears in HUD
    "HammerId": "",             // Hammerid of the weapon entity
    "ButtonClass": "",          // Classname of handler: "func_button", "logic_relay"
    "ButtonHammerId": "",       // Hammerid or targetname of handler
    "ButtonInput": "",          // Outputname of handler
    "ShowHud": true,            // Whether to show this item on the HUD
    "Cooldown": 0,              // Cooldown duration in seconds
    "MaxUses": 0                // Maxuses in one round
  },
]
```

<details>
    <summary>Clean Template</summary>

```jsonc
[
  {
    "Name": "",
    "ShortName": "",
    "HammerId": "",
    "ButtonClass": "",
    "ButtonHammerId": "",
    "ButtonInput": "",
    "ShowHud": true,
    "Cooldown": 0,
    "MaxUses": 0
  },
]
```
</details>

### BossHUD

```jsonc
{
  "MathCounterConfigs": [         // Math counter based bosses
    {
      "DisplayName": "",          // Name of boss that appears in hud
      "HpCounter": ""             // Targetname of counter
    },
    {
      "DisplayName": "",          // Name of boss that appears in hud
      "HpCounter": "",            // Targetname of main counter
      "HpBarCounter": "",         // Targetname of iterator counter
      "HpBarCounterAdd0": true,   // (unknown, leave it at default)
      "HpBarAdd": false,          // Whether iterator is reverse (OnHitMax output)
      "HpBarMin": 0,              // Iterator min value (leave empty defaults to min)
      "HpBarMax": 0               // Iterator max value (leave empty defaults to max)
    }
  ],
  "BreakableConfigs": [           // Breakable bosses
    {
      "DisplayName": "",          // Name of boss that appears in hud
      "EntityName": ""            // Targetname of breakable
    }
  ]
}
```

<details>
    <summary>Clean Template</summary>

```jsonc
{
  "MathCounterConfigs": [
    {
      "DisplayName": "",
      "HpCounter": ""
    },
    {
      "DisplayName": "",
      "HpCounter": "",
      "HpBarCounter": "",
      "HpBarCounterAdd0": true,
      "HpBarAdd": true,
      "HpBarMin": 0,
      "HpBarMax": 0
    }
  ],
  "BreakableConfigs": [
    {
      "DisplayName": "",
      "EntityName": ""
    }
  ]
}
```
</details>

## FyS

FyS has a public config [repository](https://github.com/fyscs/cs2) although not all configs are made public (e.g. EntWatch).

> [!WARNING]
> FyS config formatting requires indentation of two spaces.

### EntWatch

```jsonc
{
  "name": "",               // (string)     -> Name of item (chat)
  "shortname": "",          // (string)     -> Name of item (hud)
  "weaponId": "",           // (string)     -> Hammerid of item
  "team": 0,                // (int)        -> Item team: 3 = human, 2 = zombie
  "slot": 0,                // (int)        -> Item slot: 0 = primary, 1 = secondary, 2 = knife, 4 = C4
  "ui": true,               // (bool)       -> Whether to show this item on the HUD
  "disabled": false,        // (bool)       -> Whether to allow this item to be picked up
  "prerequesite": true,     // (bool)       -> Whether if players must fulfill prerequesite to pick up item (map level, ebans) [Default: true]
  "count": 0,               // (int)        -> How many instances of this item on the map
  "triggers": [""],         // (string[]?)  -> Array of trigger hammerids associated with the item
  "hitboxes": [""],         // (string[]?)  -> Array of hitbox hammerids associated with the item
  "abilities": [
    {
      "tag": "",            // (string?)    -> Ability name to show in chat and hud
      "type": "",           // (string)     -> Ability type: 'button', 'game_ui', 'trigger', 'relay', 'breakable', 'key'
      "event": "",          // (string)     -> Output event: 'OnPressed', 'OnPlayerUse', 'PressedAttack2', 'OnTrigger', 'OnBreak', 'OnStartTouch', 'OnEndTouch'
      "hammerId": "",       // (string)     -> Hammerid of ability
      "measure": "",        // (string?)    -> Hammerid of measure movement entity
      "container": "",      // (string?)    -> Hammerid of counter
      "maxUses": 0,         // (int)        -> Max ability uses (Mode 3/4/5 only)
      "message": true,      // (bool)       -> Whether to show ability use in chat
      "cooldown": 0,        // (int)        -> Cooldown duration of ability
      "mode": 0             // (int)        -> Mode of the ability:
                            //                 0 = None                 1 = Spam
                            //                 2 = Cooldown             3 = MaxUses
                            //                 4 = MaxUsesWithCooldown  5 = CooldownAfterUses
                            //                 6 = OnHitMinCounter      6 = OnHitMaxCounter
                            //                 7 = CounterValue
    }
  ]
}
```

<details>
    <summary>Clean Template</summary>

```jsonc
{
  "name": "",
  "shortname": "",
  "weaponId": "",
  "team": 0,
  "slot": 0,
  "ui": true,
  "disabled": false,
  "prerequesite": true,
  "count": 0,
  "triggers": [""],
  "hitboxes": [""],
  "abilities": [
    {
      "tag": "",
      "type": "",
      "event": "",
      "hammerId": "",
      "measure": "",
      "container": "",
      "maxUses": 0,
      "message": true,
      "cooldown": 0,
      "mode": 0
    }
  ]
}
```
</details>

### BossHUD

```jsonc
{
  "Proxy": true,            // (bool)       -> Whether boss health is scripted
  "Counters": [
    {
      "iterator": "",       // (string)     -> Targetname of main counter
      "backup": "",         // (string)     -> Targetname of backup counter
      "counter": "",        // (string)     -> Targetname of iterator counter
      "stages": 0.0,        // (int)        -> Number of times boss is re-triggered
      "mass": 0.0,          // (int)        -> Health per player for counter/iterator system
      "hitbox": "",         // (string?)    -> Targetname of boss hitbox
      "display": "",        // (string)     -> Name of boss that appears on hud
      "increase": false,    // (bool?)      -> Whether main counter has OnHitMax outputs
      "reverse": false,     // (bool?)      -> Whether iterator counter has OnHitMax outputs
    }
  ],
  "Breakables": [
    {
      "target": "",         // (string)     -> Targetname of boss breakable
      "count": "",          // (string?)    -> Targetname of boss iterator counter
      "display": ""         // (string)     -> Name of boss that appear on hud
    }
  ],
  "Monsters": [
    {
      "identity": "",       // (string)     -> Hammerid of counter/breakable
      "display": ""         // (string)     -> Name of boss that appears on hud
    }
  ]
}
```

<details>
    <summary>Clean Template</summary>

```jsonc
{
  "Proxy": true,
  "Counters": [
    // Full config
    {
      "iterator": "",
      "backup": "",
      "counter": "",
      "stages": 0.0,
      "mass": 0.0,
      "hitbox": "",
      "display": "",
      "increase": false,
      "reverse": false,
    },
    // Counter type boss
    {
      "iterator": "",
      "hitbox": "",
      "display": "",
    },
    // Counter, iterator, and backup type boss
    {
      "iterator": "",
      "backup": "",
      "counter": "",
      "hitbox": "",
      "display": "",
    },
    // Counter and iterator type boss
    {
      "iterator": "",
      "counter": "",
      "mass": 0.0,
      "hitbox": "",
      "display": "",
    }
  ],
  "Breakables": [
    {
      "target": "",
      "count": "",
      "display": ""
    }
  ],
  "Monsters": [
    {
      "identity": "",
      "display": ""
    }
  ]
}
```
</details>

## ZombieDen

### EntWatch

```text
"entities"
{
    "0"
    {
        "hammerid"          ""  // Hammerid of item
        "shortname_cn"      ""  // Name of item
        "cooldown"          ""  // Cooldown of item
        "maxuses"           ""  // Max uses of item
        "cooldown_knife1"   ""  // Cooldown of mouse 1 ability
        "cooldown_knife2"   ""  // Cooldown of mouse 2 ability
    }
}
```

<details>
    <summary>Clean Template</summary>

```text
"entities"
{
    "0"
    {
        "hammerid"          ""
        "shortname_cn"      ""
        "cooldown"          ""
        "maxuses"           ""
        "cooldown_knife1"   ""
        "cooldown_knife2"   ""
    }
}
```
</details>

### BossHUD

```text
"math_counter"
{
    "0"
    {
        "HP_counter"        ""  // Targetname of breakable/counter
        "HPbar_default"     ""  // Starting counter value of iterator
        "HPbar_counter"     ""  // Iterator mode: 0 = OnHitMin, 1 = OnHitMax
        "CustomText_CN"     ""  // Name of boss to display on HUD
    }
}
```

<details>
    <summary>Clean Template</summary>

```text
"math_counter"
{
    "0"
    {
        "HP_counter"        ""
        "HPbar_default"     ""
        "HPbar_counter"     ""
        "CustomText_CN"     ""
    }
}
```
</details>

## DarkerZ

### EntWatch

This version of EntWatch is publicly available [here](https://github.com/darkerz7/MS-EntWatch) (ModSharp version) or [here](https://github.com/darkerz7/EntWatchSharp) (CounterStrikeSharp version). The same config can be used for both plugins.

Find entity classnames that start with `weapon_` as a starting point for creating EntWatch configs. For each item you're going to want a new block in the root array. The format is available below.

List of available colors:
- {default} - [255,255,255,1]
- {darkred} - [255,0,0,1]
- {purple} - [128,0,128,1]
- {green} - [0,255,0,1]
- {lightgreen} - [0,255,0,1]
- {lime} - [0,255,0,1]
- {red} - [255,0,0,1]
- {grey} - [128,128,128,1]
- {team}
- {red2} - [255,0,0,1]
- {olive} - [128,128,0,1]
- {a}
- {lightblue} - [0,255,255,1]
- {blue} - [0,255,255,1]
- {d}
- {pink} - [255,105,180,1]
- {darkorange} - [255,165,0,1]
- {orange} - [255,165,0,1]
- {darkblue} - [0,0,255,1]
- {gold} - [255,255,0,1]
- {white} - [255,255,255,1]
- {yellow} - [255,255,0,1]
- {magenta} - [255,105,180,1]
- {silver} - [128,128,128,1]
- {bluegrey} - [0,255,255,1]
- {lightred} - [255,0,0,1]
- {cyan} - [0,255,255,1]
- {gray} - [128,128,128,1]
- {lightyellow} - [255,255,0,1]

```jsonc
[
  {
    "Name": "",                     // (string)     -> Name of item that appears in chat
    "ShortName": "",                // (string)     -> Name of item that appears on the HUD
    "Color": "",                    // (string)     -> Item color for chat messages (see list of colors)
    "HammerID": "",                 // (string)     -> HammerID of the weapon entity
    "GlowColor": [0,0,0,0],         // (int[4])     -> Item glow color
    "BlockPickup": false,           // (bool)       -> Whether item pickup is blocked
    "AllowTransfer": false,         // (bool)       -> Whether item can be transferred
    "ForceDrop": false,             // (bool)       -> Whether item is dropped on player death/disconnect
    "Chat": false,                  // (bool)       -> Whether item pickup/drop messages show in chat
    "Hud": false,                   // (bool)       -> Whether item is displayed on the HUD
    "TriggerID": "",                // (string?)    -> Trigger hammerid associated with item
    "UsePriority": false,           // (bool?)      -> Whether auto button press on +use detection is enabled
    "SpawnerID": "",                // (string?)    -> Hammerid of item template
    "AbilityList": [
      {
        "Name": "",                 // (string?)    -> Custom ability name
        "ButtonID": "",             // (string)     -> Hammerid of button/game_ui entity
        "ButtonClass": "",          // (string)     -> 'func_button', 'game_ui::PressedAttack', 'game_ui::PressedAttack2'
        "Filter": "",               // (string?)    -> Targetname, $attribute, context:value
        "Chat_Uses": false,         // (bool)       -> Whether item use messages show in chat
        "Mode": 0,                  // (int)        -> Item mode
                                    //                  0 = No button            1 = Spammable item
                                    //                  2 = Cooldown             3 = MaxUses
                                    //                  4 = MaxUsesWithCooldown  5 = CooldownAfterUses
                                    //                  6 = OnHitMinCounter      7 = OnHitMaxCounter
                                    //                  8 = ButtonHealth
        "MaxUses": 0,               // (int)        -> Max uses (Mode 3/4/5 only)
        "CoolDown": 0,              // (int)        -> Cooldown duration (Mode 2/4/5 only)
        "Ignore": false,            // (bool)       -> Whether to show item cooldown on HUD
        "LockItem": false,          // (bool)       -> Whether to block item activation
        "MathID": "",               // (string?)    -> Hammerid of counter (Mode 6/7 only)
        "MathNameFix": false,       // (bool?)      -> Whether to account for name fixup on counter entity
        "MathFindSpawned": false,   // (bool?)      -> Whether to look for counter after weapon spawn (For counters not in item template)
        "MathDontShowMax": false,   // (bool?)      -> Whether to show counter max value
        "MathZero": false           // (bool?)      -> Whether to allow button press when counter value is zero
      }
    ]
  }
]
```

<details>
    <summary>Clean Template</summary>

```jsonc
[
  {
    "Name": "",
    "ShortName": "",
    "Color": "",
    "HammerID": "",
    "GlowColor": [0,0,0,0],
    "BlockPickup": false,
    "AllowTransfer": false,
    "ForceDrop": false,
    "Chat": false,
    "Hud": false,
    "TriggerID": "",
    "UsePriority": false,
    "SpawnerID": "",
    "AbilityList": [
      {
        "Name": "",
        "ButtonID": "",
        "ButtonClass": "",
        "Filter": "",
        "Chat_Uses": false,
        "Mode": 0,
        "MaxUses": 0,
        "CoolDown": 0,
        "Ignore": false,
        "LockItem": false,
        "MathID": "",
        "MathNameFix": false,
        "MathFindSpawned": false,
        "MathDontShowMax": false,
        "MathZero": false
      }
    ]
  }
]
```
</details>

DarkerZ's version of EntWatch has additional commands that can be used to modify items midround. The `[hammerid]` parameter refers to the item HammerID. Parameters in `<>` are required, and parameters in `[]` are optional.

- `ew_setcooldown <int hammerid> <int buttonid> <int cooldown> [override]`: Sets cooldown duration of a button (`[override]` - whether to override cooldown if button is on cooldown)
- `ew_setmaxuses <int hammerid> <int buttonid> <int maxuses> [bool override]`: Sets max uses of a button (`[override]` - whether to override max uses if button was used)
- `ew_setuses <int hammerid> <int buttonid> <int value> [bool override]`: Sets current uses of a button (`[override]` - whether to override uses)
- `ew_addmaxuses <int hammerid> <int buttonid> [bool override]`: Adds uses to max use count of a button (`[override]` - whether to add max uses even if button use count reached max)
- `ew_setmode [int hammerid] [buttonid] [mode] [cooldown] [maxuses] <override>`: Change the mode of a button (`[override]` - whether to override button mode if already used)
- `ew_lockbutton <int hammerid> <int buttonid> <bool value>`: Lock/unlock a button
- `ew_setabilityname <int hammerid> <int buttonid> <string name>`: Sets the name of a button
- `ew_setname <int hammerid> <string name>`: Sets the name of an item that appears in chat
- `ew_setshortname <int hammerid> <string name>`: Sets the name of an item that appears on the HUD
- `ew_block <int hammerid> <bool value>`: Sets whether an item can be picked up or not
