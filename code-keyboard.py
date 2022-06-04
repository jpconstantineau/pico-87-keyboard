# SPDX-FileCopyrightText: 2022 Pierre Constantineau
# SPDX-License-Identifier: MIT
# Pico 87 Keyboard - Keyboard Firmware

"""
    Code adapted from the following sources:
    MACROPAD Hotkey (https://learn.adafruit.com/macropad-hotkeys/project-code)
    Pico Four Keypad  (https://learn.adafruit.com/pico-four-key-macropad/code-the-four-keypad)
    KNOWN ISSUES (All of this should be taken care of in while true loop):
    - crashes when more than 6 keys are pressed
    - sticky behaviour of the modifiers (Shift, ctrl, alt, gui - both left and right)
    - "Layer" key is not doing anything
"""

# Import necessary modules/libraries
import board
import keypad
from digitalio import DigitalInOut, Direction
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode as KC
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


# LED Setup.
led1 = DigitalInOut(board.GP27)
led1.direction = Direction.OUTPUT

led2 = DigitalInOut(board.GP28)
led2.direction = Direction.OUTPUT

# Switch Matrix Setup.
keys = keypad.KeyMatrix(
            row_pins=(board.GP18,
                        board.GP19,
                        board.GP20,
                        board.GP21,
                        board.GP22,
                        board.GP26),
            column_pins=(board.GP0,
                        board.GP1,
                        board.GP2,
                        board.GP3,
                        board.GP4,
                        board.GP5,
                        board.GP6,
                        board.GP7,
                        board.GP8,
                        board.GP9,
                        board.GP10,
                        board.GP11,
                        board.GP12,
                        board.GP13,
                        board.GP14,
                        board.GP15,
                        board.GP16,
                        board.GP17),
            columns_to_anodes=True,
        )


kpd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kpd)


#[ # Layer 0 QWERTY
#KC.GRAVE, KC.N1, KC.N2, KC.N3,  KC.N4,  KC.N5, KC.N6,  KC.N7, KC.N8, KC.N9,   KC.N0,   KC.MINUS, KC.EQUAL, KC.NO,     KC.BSPC, KC.INS,  KC.HOME,       KC.PGUP,
#KC.TAB,   KC.NO,  KC.Q,  KC.W,   KC.E,   KC.R,  KC.T,   KC.Y,  KC.U,  KC.I,    KC.O,    KC.P,     KC.LBRC,  KC.RBRC,   KC.BSLS, KC.DEL, KC.END,       KC.PGDN,
#KC.CAPS,  KC.NO,    KC.A,  KC.S,   KC.D,   KC.F,  KC.G,   KC.H,  KC.J,  KC.K,    KC.L,    KC.SCLN,  KC.QUOT,  KC.ENT,    KC.NO, KC.NO,      KC.NO,      KC.NO,
#KC.NO,    KC.LSHIFT, KC.Z,  KC.X,   KC.C,   KC.V,  KC.B,   KC.N,  KC.M,  KC.COMM, KC.DOT,  KC.SLSH,  KC.NO,    KC.RSHIFT, KC.NO,    KC.NO,   KC.UP,   KC.NO,
#KC.LCTL,  KC.LGUI,   KC.NO, KC.LALT, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO, KC.NO,   KC.RALT, KC.RGUI,  KC.NO,    KC.MO(1),     KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT,
#  ],


# See here for definition of keycodes: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html
keymap = [
    ("Esc", [KC.ESCAPE]),("n/a", [0]),("F1", [KC.F1]),("F2", [KC.F2]),("F3", [KC.F3]),("F4", [KC.F4]),("n/a", [0]),("F5", [KC.F5]),("F6", [KC.F6]),("F7", [KC.F7]),("F8", [KC.F8]),
    ("F9", [KC.F9]),("F10", [KC.F10]),("F11", [KC.F11]),("F12", [KC.F12]),("PSCREEN", [KC.PRINT_SCREEN]),("SCROLLLOCK", [KC.SCROLL_LOCK]),("PAUSE", [KC.PAUSE]), # end of row 1
    ("GRAVE", [KC.GRAVE_ACCENT]),("1", [KC.ONE]),("2", [KC.TWO]),("3", [KC.THREE]),("4", [KC.FOUR]),("5", [KC.FIVE]),("6", [KC.SIX]),("7", [KC.SEVEN]),("8", [KC.EIGHT]),
    ("9", [KC.NINE]),("0", [KC.ZERO]),("MINUS", [KC.MINUS]),("EQUAL", [KC.EQUALS]),("n/a", [0]),("BACKSPACE", [KC.BACKSPACE]),("INSERT", [KC.INSERT]),("HOME", [KC.HOME]),("PAGE_UP", [KC.PAGE_UP]), # end of row 2
    ("TAB", [KC.TAB]),("n/a", [0]),("Q", [KC.Q]),("W", [KC.W]),("E", [KC.E]),("R", [KC.R]),("T", [KC.T]),("Y", [KC.Y]),("U", [KC.U]),("I", [KC.I]),("O", [KC.O]),
    ("P", [KC.P]),("{", [KC.LEFT_BRACKET]),("}", [KC.RIGHT_BRACKET]),("\\", [KC.BACKSLASH]),("DELETE", [KC.DELETE]),("END", [KC.END]),("PAGE_DOWN", [KC.PAGE_DOWN]), # end of row 3
    ("CAPS", [KC.CAPS_LOCK]),("n/a", [0]),("A", [KC.A]),("S", [KC.S]),("D", [KC.D]),("F", [KC.F]),("G", [KC.G]),("H", [KC.H]),("J", [KC.J]),("K", [KC.K]),("L", [KC.L]),
    (";", [KC.SEMICOLON]),("'", [KC.QUOTE]),("ENTER", [KC.ENTER]),("n/a", [0]),("n/a", [0]),("n/a", [0]),("n/a", [0]), # end of row 4
    ("n/a", [0]),("LSHIFT", [KC.LEFT_SHIFT]),("Z", [KC.Z]),("X", [KC.X]),("C", [KC.C]),("V", [KC.V]),("B", [KC.B]),("N", [KC.N]),("M", [KC.M]),(",", [KC.COMMA]),(".", [KC.PERIOD]),
    ("/", [KC.FORWARD_SLASH]),("n/a", [0]),("RSHIFT", [KC.RIGHT_SHIFT]),("n/a", [0]),("n/a", [0]),("UP", [KC.UP_ARROW]),("n/a", [0]), # end of row 5
    ("LCTL", [KC.LEFT_CONTROL]),("LGUI", [KC.LEFT_GUI]),("n/a", [0]),("LALT", [KC.LEFT_ALT]),("n/a", [0]),("n/a", [0]),("SPACE", [KC.SPACE]),("n/a", [0]),("n/a", [0]),("n/a", [0]),
    ("RALT", [KC.RIGHT_ALT]),("RGUI", [KC.RIGHT_GUI]),("n/a", [0]),("FnKey", [0]),("RCTL", [KC.RIGHT_CONTROL]),("LEFT", [KC.LEFT_ARROW]),("DOWN", [KC.DOWN_ARROW]),("RIGHT", [KC.RIGHT_ARROW]), # end of row 6
]

print("keymap:")
for key in keymap:
    print("\t", key[0])

i = 0
while True:
    key_event = keys.events.get()
    if key_event:
        print(key_event)
        if key_event.pressed:
            i = i + 1
            print(keymap[key_event.key_number][0])
            sequence = keymap[key_event.key_number][1]
            for item in sequence:
                if isinstance(item, int):
                    if item >= 0:
                        kpd.press(item)
                    else:
                        kpd.release(-item)
                else:
                    keyboard_layout.write(item)
        else:
            i = i - 1
            # Release any still-pressed modifier keys
            for item in sequence:
                if isinstance(item, int) and item >= 0:
                    kpd.release(item)
    if i == 0:
        led1.value = False
        led2.value = False
    else:
        if i == 1:
            led1.value = True
            led2.value = False
        else:
            led1.value = True
            led2.value = True
