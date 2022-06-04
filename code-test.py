# SPDX-FileCopyrightText: 2022 Pierre Constantineau
# SPDX-License-Identifier: MIT
# Pico 87 Keyboard - Test Firmware

# Import necessary modules/libraries
import board
import keypad
from digitalio import DigitalInOut, Direction

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

# scan the matrix and turn on the LEDs when pressing keys
# LED 1 OFF LED 2 OFF:  0 keys pressed
# LED 1 ON  LED 2 OFF:  1 key pressed
# LED 1 ON  LED 2 ON:   2 or more keys pressed

i = 0
while True:
    key_event = keys.events.get()
    if key_event:
        print(key_event)
        if key_event.pressed:
            i = i + 1
        else:
            i = i - 1

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
