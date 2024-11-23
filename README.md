# Aarts-Volume-Control
## Dedicated Volume Control with QT Py RP2040 and Rotary Encoder

This CircuitPython project adds a dedicated volume control to a PC using an Adafruit QT Py RP2040 and a Stemma QT Rotary Encoder. The rotary encoder adjusts the system volume, while pressing its button toggles mute. 

Originally created as a fun and functional upgrade for my 5-year-old son's PC setup, this project is perfect for anyone looking to build a simple, user-friendly hardware volume controller.

### Features
- **Volume Control**: Rotate the encoder to increase or decrease volume.
- **Mute Toggle**: Press the encoder button to toggle mute.
- **USB HID Integration**: Functions seamlessly as a USB Human Interface Device (HID).

### Hardware
- [Adafruit QT Py RP2040](https://www.adafruit.com/product/4900)
- [Adafruit Stemma QT Rotary Encoder Breakout Board](https://www.adafruit.com/product/5880)

### Software
- CircuitPython with the following libraries:
  - `adafruit_seesaw` for rotary encoder management.
  - `adafruit_hid` for USB HID consumer control.
