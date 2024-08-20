layers = {
    "first":1,
    "second":2,
    "third":3
}

colors = {
    "random": 0,
    "red": 1, #ok
    "yellow": 2,
    "bight_green": 3,
    "dark_green": 4,
    "cyan": 5,
    "blue": 6,
    "violet": 7,
    "white": 8,
}

modes = {
    "off": 0,
    "solid": 1,
    "blink": 2,
    "breathing": 3,
    "rainbow": 4,
    "snake": 5,
}

keytypes = {
    "None" : 0,
    "Basic" : 1,
    "Multimedia" : 2,
    "Mouse" : 3,
    "LED" : 8
}

actions = {
    "None" : 0,
    "Key1" : 1,
    "Key2" : 2,
    "Key3" : 3,
    "Key4" : 4,
    "Key5" : 5,
    "Key6" : 6,
    "Key7" : 7,
    "Key8" : 8,
    "Key9" : 9,
    "Key10" : 10,
    "Key11" : 11,
    "Key12" : 12,
    "Knob1Left" : 13,
    "Knob1Push" : 24,
    "Knob1Right" : 25,
    "Knob2Left" : 26,
    "Knob2Push" : 27,
    "Knob2Right" : 28,
    "Knob3Left" : 29,
    "Knob3Push" : 30,
    "Knob3Right" : 31,
    "ledconfig" : 176
}

keycodes = {
    "A" : 4,
    "B" : 5,
    "C" : 6,
    "D" : 7,
    "E" : 8,
    "F" : 9,
    "G" : 10,
    "H" : 11,
    "I" : 12,
    "J" : 13,
    "K" : 14,
    "L" : 15,
    "M" : 16,
    "N" : 17,
    "O" : 18,
    "P" : 19,
    "Q" : 20,
    "R" : 21,
    "S" : 22,
    "T" : 23,
    "U" : 24,
    "V" : 25,
    "W" : 26,
    "X" : 27,
    "Y" : 28,
    "Z" : 29,
    "D1" : 30,
    "D2" : 31,
    "D3" : 32,
    "D4" : 33,
    "D5" : 34,
    "D6" : 35,
    "D7" : 36,
    "D8" : 37,
    "D9" : 38,
    "D0" : 39,
    "Enter" : 40,
    "Esc" : 41,
    "Backspace" : 42,
    "Tab" : 43,
    "SpaceKey" : 44,
    "Minus" : 45,
    "Plus" : 46,
    "OpenBracket" : 47,
    "CloseBracket" : 48,
    "Pipe" : 49,
    "Colon" : 51,
    "Backslash" : 52,
    "Tilde" : 53,
    "Clear" : 54,
    "Period" : 55,
    "Question" : 56,
    "CapsLock" : 57,
    "F1" : 58,
    "F2" : 59,
    "F3" : 60,
    "F4" : 61,
    "F5" : 62,
    "F6" : 63,
    "F7" : 64,
    "F8" : 65,
    "F9" : 66,
    "F10" : 67,
    "F11" : 68,
    "F12" : 69,
    "PrtSc" : 70,
    "ScrollLock" : 71,
    "PauseBreak" : 72,
    "Insert" : 73,
    "Home" : 74,
    "PgUp" : 75,
    "Del" : 76,
    "End" : 77,
    "PgDn" : 78,
    "ArrowRight" : 79,
    "ArrowLeft" : 80,
    "ArrowDown" : 81,
    "ArrowUp" : 82,
    "Num" : 83,
    "NumDiv" : 84,
    "NumMul" : 85,
    "NumSub" : 86,
    "NumAdd" : 87,
    "Num1" : 89,
    "Num2" : 90,
    "Num3" : 91,
    "Num4" : 92,
    "Num5" : 93,
    "Num6" : 94,
    "Num7" : 95,
    "Num8" : 96,
    "Num9" : 97,
    "Num0" : 98,
    "NumDec" : 99,
    "NumEnter" : 100,
    "App" : 101,
    "IsoPlus1" : 102,
    "None" : 0
}

modifiers = {
    "Ctrl": 1,
    "Shift": 1 << 1,
    "Alt": 1 << 2,
    "Win": 1 << 3,
    "LeftCtrl": 1,
    "LeftShift": 1 << 1,
    "LeftAlt": 1 << 2,
    "LeftWin": 1 << 3,
    "RightCtrl": 1 << 4,
    "RightShift": 1 << 5,
    "RightAlt": 1 << 6,
    "RightWin": 1 << 7,
    "None": 0
}

mouse_configurations = {
    "MouseLeftKey": [0, 1, 0, 0, 0],
    "MouseMiddle": [0, 4, 0, 0, 0],
    "MouseRight": [0, 2, 0, 0, 0],
    "MouseWheelUp": [0, 0, 0, 0, 1],
    "MouseWheelDn": [0, 0, 0, 0, 255],
    "CtrlMouseUp": [1, 0, 0, 0, 1],
    "CtrlMouseDn": [1, 0, 0, 0, 255],
    "ShiftMouseUp": [2, 0, 0, 0, 1],
    "ShiftMouseDn": [2, 0, 0, 0, 255],
    "AltMouseUp": [4, 0, 0, 0, 1],
    "AltMouseDn": [4, 0, 0, 0, 255]
}

media_key_values = {
    "PlayPause": {
        0: {"B1": 64, "B2": 0},
        2: {"B1": 0, "B2": 4},
        3: {"B1": 205, "B2": 0}
    },

    "NextTrack": {
        0: {"B1": 0, "B2": 1},
        2: {"B1": 0, "B2": 10},
        3: {"B1": 181, "B2": 0}
    },
    "PrevTrack": {
        0: {"B1": 128, "B2": 0},
        2: {"B1": 0, "B2": 11},
        3: {"B1": 182, "B2": 0}
    },
    "VolMute": {
        0: {"B1": 4, "B2": 0},
        2: {"B1": 0, "B2": 1},
        3: {"B1": 226, "B2": 0}
    },
    "6": {
        0: {"B1": 2, "B2": 0},
        2: {"B1": 64, "B2": 0},
        3: {"B1": 233, "B2": 0}
    },
    "VolDn": {
        0: {"B1": 1, "B2": 0},
        2: {"B1": 128, "B2": 0},
        3: {"B1": 234, "B2": 0}
    },
    "Stop":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 183, "B2": 0}
    },
    "Computer":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 148, "B2": 1}
    },
    "ScreenBritnessUp":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 111, "B2": 0}
    },
    "ScreenBritnessDn":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 111, "B2": 0}
    },
    "Multimedial":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 131, "B2": 1}
    },
    "Calc":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 146, "B2": 1}
    },
    "Home":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 35, "B2": 2}
    },
    "Email":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 138, "B2": 1}
    },
    "BassUp":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 82, "B2": 1}
    },
    "TrebleUp":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 84, "B2": 1}
    },
    "TrebleDn":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 85, "B2": 1}
    },
    "PgRefresh":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 39, "B2": 2}
    },
    "PgForward":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 37, "B2": 2}
    },
    "PgBack":{
        0: {"B1": 0, "B2": 0},
        2: {"B1": 0, "B2": 0},
        3: {"B1": 36, "B2": 2}
    }
}
