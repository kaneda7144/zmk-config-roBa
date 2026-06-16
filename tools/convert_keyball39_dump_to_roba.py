from __future__ import annotations

import argparse
import json
from pathlib import Path


KEYBALL_VISIBLE_POSITIONS = {
    "Q": "0,0",
    "W": "0,1",
    "E": "0,2",
    "R": "0,3",
    "T": "0,4",
    "A": "1,0",
    "S": "1,1",
    "D": "1,2",
    "F": "1,3",
    "G": "1,4",
    "Z": "2,0",
    "X": "2,1",
    "C": "2,2",
    "V": "2,3",
    "B": "2,4",
    "LCTRL": "3,0",
    "LGUI": "3,1",
    "LALT": "3,2",
    "TAB_THUMB": "3,3",
    "SPACE_THUMB": "3,4",
    "SHIFT_THUMB": "3,5",
    "Y": "4,4",
    "U": "4,3",
    "I": "4,2",
    "O": "4,1",
    "P": "4,0",
    "H": "5,4",
    "J": "5,3",
    "K": "5,2",
    "L": "5,1",
    "RIGHT_OUTER_HOME": "5,0",
    "N": "6,4",
    "M": "6,3",
    "RIGHT_BOTTOM_3": "6,2",
    "RIGHT_BOTTOM_4": "6,1",
    "RIGHT_BOTTOM_5": "6,0",
    "ESC_THUMB": "7,0",
    "ENTER_THUMB": "7,4",
    "BSPC_THUMB": "7,5",
}

ROBA_ROWS = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    [
        "A",
        "S",
        "D",
        "F",
        "G",
        "ROBA_EXTRA_L1",
        "ROBA_EXTRA_R1",
        "H",
        "J",
        "K",
        "L",
        "RIGHT_OUTER_HOME",
    ],
    [
        "Z",
        "X",
        "C",
        "V",
        "B",
        "ROBA_EXTRA_L2",
        "ROBA_EXTRA_R2",
        "N",
        "M",
        "RIGHT_BOTTOM_3",
        "RIGHT_BOTTOM_4",
        "RIGHT_BOTTOM_5",
    ],
    [
        "LCTRL",
        "LGUI",
        "LALT",
        "TAB_THUMB",
        "SPACE_THUMB",
        "SHIFT_THUMB",
        "BSPC_THUMB",
        "ENTER_THUMB",
        "ESC_THUMB",
    ],
]

BASIC_KEYCODES = {
    0x0000: "&none",
    0x0001: "&trans",
    0x0004: "&kp A",
    0x0005: "&kp B",
    0x0006: "&kp C",
    0x0007: "&kp D",
    0x0008: "&kp E",
    0x0009: "&kp F",
    0x000A: "&kp G",
    0x000B: "&kp H",
    0x000C: "&kp I",
    0x000D: "&kp J",
    0x000E: "&kp K",
    0x000F: "&kp L",
    0x0010: "&kp M",
    0x0011: "&kp N",
    0x0012: "&kp O",
    0x0013: "&kp P",
    0x0014: "&kp Q",
    0x0015: "&kp R",
    0x0016: "&kp S",
    0x0017: "&kp T",
    0x0018: "&kp U",
    0x0019: "&kp V",
    0x001A: "&kp W",
    0x001B: "&kp X",
    0x001C: "&kp Y",
    0x001D: "&kp Z",
    0x001E: "&kp NUMBER_1",
    0x001F: "&kp NUMBER_2",
    0x0020: "&kp NUMBER_3",
    0x0021: "&kp NUMBER_4",
    0x0022: "&kp NUMBER_5",
    0x0023: "&kp NUMBER_6",
    0x0024: "&kp NUMBER_7",
    0x0025: "&kp NUMBER_8",
    0x0026: "&kp NUMBER_9",
    0x0027: "&kp NUMBER_0",
    0x0028: "&kp ENTER",
    0x0029: "&kp ESCAPE",
    0x002A: "&kp BACKSPACE",
    0x002B: "&kp TAB",
    0x002C: "&kp SPACE",
    0x002D: "&kp MINUS",
    0x002E: "&kp EQUAL",
    0x002F: "&kp LEFT_BRACKET",
    0x0030: "&kp RIGHT_BRACKET",
    0x0031: "&kp BACKSLASH",
    0x0033: "&kp SEMICOLON",
    0x0034: "&kp SQT",
    0x0035: "&kp GRAVE",
    0x0036: "&kp COMMA",
    0x0037: "&kp DOT",
    0x0038: "&kp SLASH",
    0x003A: "&kp F1",
    0x003B: "&kp F2",
    0x003C: "&kp F3",
    0x003D: "&kp F4",
    0x003E: "&kp F5",
    0x003F: "&kp F6",
    0x0040: "&kp F7",
    0x0041: "&kp F8",
    0x0042: "&kp F9",
    0x0043: "&kp F10",
    0x0044: "&kp F11",
    0x0045: "&kp F12",
    0x004B: "&kp PAGE_UP",
    0x004C: "&kp DEL",
    0x004E: "&kp PAGE_DOWN",
    0x004F: "&kp RIGHT_ARROW",
    0x0050: "&kp LEFT_ARROW",
    0x0051: "&kp DOWN_ARROW",
    0x0052: "&kp UP_ARROW",
    0x0054: "&kp KP_SLASH",
    0x0055: "&kp KP_ASTERISK",
    0x0056: "&kp KP_MINUS",
    0x0057: "&kp KP_PLUS",
    0x0067: "&kp KP_EQUAL",
    0x0087: "&kp INT1",
    0x0089: "&kp INT3",
    0x00D1: "&mkp MB1",
    0x00D2: "&mkp MB2",
    0x00D3: "&mkp MB3",
    0x00E0: "&kp LCTRL",
    0x00E1: "&kp LEFT_SHIFT",
    0x00E2: "&kp LEFT_ALT",
    0x00E3: "&kp LEFT_WIN",
    0x00E6: "&kp RIGHT_ALT",
    0x00E7: "&kp RIGHT_WIN",
}

MODIFIERS = {
    0x01: "LC",
    0x02: "LS",
    0x04: "LA",
    0x08: "LG",
    0x10: "RC",
    0x20: "RS",
    0x40: "RA",
    0x80: "RG",
}

MACRO_KEYCODES = {
    0x7700: "&macro_0",
    0x7701: "&macro_1",
    0x7702: "&macro_2",
    0x7703: "&macro_3",
    0x7704: "&macro_4",
}


def zmk_key_name(binding: str) -> str:
    if not binding.startswith("&kp "):
        raise ValueError(f"Cannot use non-keypress binding as key name: {binding}")
    return binding.removeprefix("&kp ")


def apply_mods(mod_mask: int, key_name: str) -> str:
    for bit, name in MODIFIERS.items():
        if mod_mask & bit:
            key_name = f"{name}({key_name})"
    return key_name


def convert_keycode(code: int) -> str:
    if code in MACRO_KEYCODES:
        return MACRO_KEYCODES[code]

    if 0x4000 <= code <= 0x4FFF:
        layer = (code >> 8) & 0x0F
        base = code & 0xFF
        if layer == 3 and base == 0x29:
            return f"&fast_lt {layer} {zmk_key_name(convert_keycode(base))}"
        return f"&lt {layer} {zmk_key_name(convert_keycode(base))}"

    if 0x2000 <= code <= 0x3FFF:
        mod_mask = (code >> 8) & 0x1F
        base = code & 0xFF
        return f"&mt {apply_mods(mod_mask, '').strip('()')} {zmk_key_name(convert_keycode(base))}"

    if 0x0100 <= code <= 0x1FFF:
        mod_mask = (code >> 8) & 0xFF
        base = code & 0xFF
        return f"&kp {apply_mods(mod_mask, zmk_key_name(convert_keycode(base)))}"

    if code in BASIC_KEYCODES:
        return BASIC_KEYCODES[code]

    return f"&none /* unsupported_qmk_0x{code:04X} */"


def layer_binding(layer: dict[str, int], key: str, layer_index: int) -> str:
    if key == "ROBA_EXTRA_L1":
        return "&mo 6" if layer_index == 0 else "&trans"
    if key.startswith("ROBA_EXTRA_"):
        return "&none" if layer_index == 0 else "&trans"
    pos = KEYBALL_VISIBLE_POSITIONS[key]
    return convert_keycode(layer[pos])


def format_rows(rows: list[list[str]]) -> str:
    max_width = max(len(item) for row in rows for item in row)
    lines = []
    for row in rows:
        lines.append(" ".join(item.ljust(max_width) for item in row).rstrip())
    return "\n".join(lines)


def zmk_layer(name: str, rows: list[list[str]], sensor: str | None = None) -> str:
    body = format_rows(rows)
    sensor_block = f"\n\n            sensor-bindings = <{sensor}>;" if sensor else ""
    return f"""        {name} {{
            bindings = <
{body}
            >;{sensor_block}
        }};"""


def build_rows(layer: dict[str, int], layer_index: int) -> list[list[str]]:
    return [[layer_binding(layer, key, layer_index) for key in row] for row in ROBA_ROWS]


def build_keymap(dump: dict) -> str:
    layers = dump["keycodes"]
    generated_at = dump.get("generatedAt", "unknown")
    macro_rows = [
        "<&kp NUMBER_0 &kp NUMBER_0>",
        "<&kp LS(NUMBER_8) &kp LS(NUMBER_9) &kp LEFT_ARROW>",
        "<&kp RIGHT_BRACKET &kp BACKSLASH &kp LEFT_ARROW>",
        "<&kp LS(RIGHT_BRACKET) &kp LS(BACKSLASH) &kp LEFT_ARROW>",
        "<&kp LS(COMMA) &kp LS(DOT) &kp LEFT_ARROW>",
    ]

    layer_blocks = [
        zmk_layer("default_layer", build_rows(layers[0], 0), "&inc_dec_kp PG_UP PAGE_DOWN"),
        zmk_layer("keyball_layer_1", build_rows(layers[1], 1)),
        zmk_layer("keyball_layer_2", build_rows(layers[2], 2)),
        zmk_layer("keyball_layer_3", build_rows(layers[3], 3)),
        zmk_layer(
            "MOUSE",
            [
                ["&trans"] * 10,
                ["&trans"] * 7 + ["&trans", "&mkp MB1", "&mkp MB3", "&mkp MB2", "&trans"],
                ["&trans"] * 12,
                ["&trans"] * 9,
            ],
        ),
        zmk_layer("SCROLL", [["&trans"] * len(row) for row in ROBA_ROWS]),
        zmk_layer(
            "settings_layer",
            [
                ["&trans", "&trans", "&trans", "&trans", "&trans", "&bt BT_SEL 0", "&bt BT_SEL 1", "&bt BT_SEL 2", "&bt BT_SEL 3", "&bt BT_SEL 4"],
                ["&trans"] * 12,
                ["&trans", "&kp NUMBER_1", "&kp NUMBER_2", "&kp NUMBER_3", "&trans", "&trans", "&bootloader", "&trans", "&trans", "&trans", "&trans", "&bt BT_CLR"],
                ["&trans", "&trans", "&trans", "&trans", "&trans", "&trans", "&trans", "&trans", "&bt BT_CLR_ALL"],
            ],
        ),
    ]

    macros = "\n\n".join(
        f"""        macro_{i}: macro_{i} {{
            compatible = "zmk,behavior-macro";
            #binding-cells = <0>;
            wait-ms = <30>;
            tap-ms = <40>;
            bindings = {bindings};
        }};"""
        for i, bindings in enumerate(macro_rows)
    )

    return f"""#include <behaviors.dtsi>
#include <dt-bindings/zmk/bt.h>
#include <dt-bindings/zmk/keys.h>
#include <dt-bindings/zmk/pointing.h>

// Generated from Keyball39 VIA dump captured at {generated_at}.
// Keyball39 has 39 visible keys; ROBA's extra inner keys are reserved for settings/unused.

&mt {{
    flavor = "balanced";
    quick-tap-ms = <0>;
}};

&trackball {{
    automouse-layer = <4>;
    scroll-layers = <3 5>;
}};

/ {{
    behaviors {{
        fast_lt: fast_layer_tap {{
            compatible = "zmk,behavior-hold-tap";
            #binding-cells = <2>;
            flavor = "tap-preferred";
            tapping-term-ms = <200>;
            quick-tap-ms = <0>;
            hold-while-undecided;
            bindings = <&mo>, <&kp>;
        }};
    }};

    macros {{
{macros}
    }};

    keymap {{
        compatible = "zmk,keymap";

{chr(10).join(layer_blocks)}
    }};
}};
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dump", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    dump = json.loads(args.dump.read_text(encoding="utf-8"))
    if dump.get("format") != "keyball39-via-dump-v1":
        raise SystemExit("Unsupported dump format")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_keymap(dump), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
