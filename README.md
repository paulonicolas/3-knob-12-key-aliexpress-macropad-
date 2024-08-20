
# 3 KNOB 12 KEY ALIEXPRESS MACROPAD PROGRAM FOR LINUX
This program was developed to cooverage the configuration for Linux (It could also be implemented on Windows or Mac.) and is not complete in a visual mode but can be a point to start a more complex deleloped.

![Keyboar 12 keys 3 knobs](https://github.com/paulonicolas/3-knob-12-key-aliexpress-macropad-/blob/9f7028b14a91adddaf28f5a0c9d023e06d975d06/python_app/12x3knob_.jpg)
## Some things to keep in mind:
- HID is a method for comunicate with a keyboard.
- Python provide a library to use this comunication.
- you need a VENDOR ID and PRODUCT ID from keyboard, with lsusb in a terminal you can know (in this case VENDOR ID=0x1189 and PRODUCT ID=0x8842 ).
  ```bash
  $ lsusb
  ...
  Bus 001 Device 018: ID 1189:8842 Acer Communications & Multimedia USB Composite Device
  ...
- In linux you need provide a permissions (this is programed)
- To send a instruction you can generate an array for 64 bytes (only are necesaries about 15 bytes aprox), in code is explained how you do it.
- The array is as follows (see function get_report()):
  ```bash
        --data = [0] * 64  # size of array
        --data[0] = reportid  # reportid (fixed: 3)
        --data[1] = 254  # fixed byte
        --data[2] = inputAction   # action - key to program (SEE dict input actions in info.py)
        --data[3] = layer  # Number of layer (1,2 o 3) (SEE dict layers in info.py)
        --data[4] = keytype  # keytype: LED, MULTIMEDIA, MOUSE, BASIC (SEE dict keytypes in info.py)
        --data[5] = delay & 0xFF  # delay 
        --data[6] = (delay >> 8) & 0xFF  # delay
        --data[7] = 0 # default
        --data[8] = 0 # default
        --data[9] = 0 # default
        --data[10] = len(data_list) # length from data list depend to type keytype (see the code config/)
        --data 11 to n:  depends to type keytype (see the examples from usb_config_moc_V1.py, arrays: data_led, data_key, data_media and data_mouse )
   ```
- In function send_hid_report() you can send the reports generates with get_report.

## INSTALATION:
- Preferent with a enviroment for python.
- python -m venv env
- source xxx/xx/env/bin/activate
- pip install hidapi
  
## THINGS THAT ARE MISSING:
- Read the device (only you can write).
- Configure the knobs: I couldn't find the codes for the knobs.
- The visual experience in linux is not finished.
  
<a href="https://www.buymeacoffee.com/paulojarafe" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
