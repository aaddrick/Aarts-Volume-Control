"""
CircuitPython Script for Dedicated Volume Control

Hardware:
- Adafruit QT Py RP2040 (https://www.adafruit.com/product/4900)
- Adafruit Stemma QT Rotary Encoder Breakout Board (https://www.adafruit.com/product/5880)

Description:
This script uses the QT Py RP2040 and the Stemma QT Rotary Encoder to provide a dedicated 
volume control for a PC. The rotary encoder adjusts the volume, and pressing the encoder's 
button toggles mute.

This project was created as a fun and functional addition for my 5-year-old son's PC setup.

Libraries Used:
- adafruit_seesaw for handling the rotary encoder
- adafruit_hid for USB HID consumer control (volume/mute)

Circuit Connection:
- The Stemma QT Rotary Encoder is connected via I2C to the QT Py RP2040's Stemma QT port.

Author: Aaddrick
Date: 11/23/2024
"""


import board
import time
from adafruit_seesaw import seesaw, rotaryio, digitalio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

i2c = board.STEMMA_I2C()  
seesaw = seesaw.Seesaw(i2c, addr=0x36)

# Check if we have the right firmware
seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")
    while True:
        pass

# Initialize the rotary encoder
encoder = rotaryio.IncrementalEncoder(seesaw)

# Configure seesaw pin for button with internal pull-up
seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
button = digitalio.DigitalIO(seesaw, 24)

# Initialize HID
cc = ConsumerControl(usb_hid.devices)

# Initialize state variables
last_position = 0
button_held = False

while True:
    # negate the position to make clockwise rotation positive
    position = -encoder.position
    
    if position != last_position:
        if position > last_position:
            print("Volume up")
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        else:
            print("Volume down")
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        last_position = position
    
    # Handle button press (mute)
    if not button.value and not button_held:
        print("Button pressed - Mute toggle")
        cc.send(ConsumerControlCode.MUTE)
        button_held = True
    
    if button.value and button_held:
        print("Button released")
        button_held = False
    
    time.sleep(0.01)
