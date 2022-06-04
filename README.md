# Pico 87 keyboard build notes

This is a repository documenting the process for building the Pico 87 keyboard, testing it and getting a firmware loaded up. 

The Pico 87 is an inexpensive TKL keyboard designed by Ian Dunn and is available on [kickstarter](https://www.kickstarter.com/projects/bi-vfd-clock/the-bolt-industries-pico-87-mechanical-keyboard).

With minor exceptions, it uses all through-hole components and is a relatively easy keyboard to build as a first DIY keyboard.


## Build Notes

The [Build Guide](https://www.boltind.com/?page_id=524) has enough information for someone familiar with electronic kits to be able to be able to build it.  The guide has the schematics, something which is quite useful when building and writing the test firmware.


## Test Firmware

You don't need the Arduino IDE to load a test firmware onto the keyboard.  I recommend using CirCuitPython.  It's really easy to get it setup.  Learn more about CircuitPython [here](https://circuitpython.org/).

- Download the circuitpython build for the Raspberry Pi Pico from [here](https://circuitpython.org/board/raspberry_pi_pico/)
- Put the Pico in "Bootloader mode". Do this by connecting the USB while pressing the BootSel button (either on the Pico itself or the one accessible on the left side of the keyboard). A new mass storage device should show up on your computer.
- Copy (drag/drop) the CircuitPython UF2 file `adafruit-circuitpython-raspberry_pi_pico-en_US-7.3.0.uf2` into the Raspberry Pi Pico "RPI-RP2" drive that just showed up.  This will flash CircuitPython to the Raspberry Pi Pico.  Note: 7.3 was the current release at the time of writing this.
- Once flashed, the keyboard should reboot. If it doesn't, disconnect and reconnect the USB cable.  On reboot, you should see a new mass storage device called "CIRCUITPY" with a folder called "lib" and a python code file named "code.py".   
- Download the library bundle from the [CircuitPython library page](https://circuitpython.org/libraries).  You should get a zip file called "adafruit-circuitpython-bundle-7.x-mpy-20220602.zip". Note: 20220602 was the current release at the time of writing this.
- Uncompress the Zip bundle.
- Navigate into the folder where the zip was uncompressed until you get into the "lib" folder.
- copy the `adafruit_hid` folder into the `lib` folder of the Raspberry Pi Pico "CIRCUITPY" drive.  On the Raspberry Pi Pico, you shoud have 8 files in the `/lib/adafruit_hid` folder.  This is the library we will need for the keyboard firmware.
- open up the code.py file in an editor
- replace the content with the file named `code-test.py` from this repo.

## Using the Test Firmware

Once you have the steps above completed, you can press each and every key on the keyboard to test whether they work fine.  When pressing a single key, LED 1 should light up. This the one between "F1" and "F2".  When pressing more than 1 key, both LEDs should light up.

To verify that your keyboard works as expected, follow these steps:
- Press each key, 1 at a time.  Each keypress should only light up LED 1.  If both LEDs are lit-up when pressing a single key, you have a short somewhere... if no LED light up you need to check if the LED is wired correctly, followed by all of your diodes (you can set `columns_to_anodes` to False to flip the polarity of the matrix diodes).
- Press multiple keys at a time.  LED 2 should also light up.

## Keyboard firmware

Once you have tested your hardware, you can load a keyboard firmware.  As a starting point, you can copy the content of the `code-keyboard.py` from this repo into `code.py`.  It has a number of known issues (see top of file).

I recommend using KMK instead.  Refer to the [KMK repository](https://github.com/KMKfw/kmk_firmware) for information how to install KMK and configure it for the keyboard.
