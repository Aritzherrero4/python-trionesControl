# trionesControl

This module implements the triones protocol reverse engineered by [madhead](https://github.com/madhead) with python, offering a programmatic way to control these kind of lights without needing the app on your phone. To learn more about the protocol, please read the following specification:

* [madhead - saberlight/protocols/Triones/protocol.md](https://github.com/madhead/saberlight/blob/master/protocols/Triones/protocol.md)

## Requirements

This package only works on Linux, it uses pygatt and depends on blueZ.

The package has been tested in python 3 (3.8.5) but it may work on previous versions, even python 2.7, as long as [pygatt requirements](https://github.com/peplin/pygatt#requirements) are met.

## Installation

Install ``trionesControl`` with pip from PyPI:

    pip install trionesControl

This will install all the dependencies used by this package and ``pexpect``, an optional ``pygatt`` needed to use it's BlueZ backend.

## Documentation

### Connexion handling

* ``connect(MAC)``: Connect to the device with the mac address specified.

* ``disconnect(device)``: Disconnects from the specified device.

### LED Control

* ``powerOn(device)``: Powers on the device, the LEDs will turn on.

* ``powerOff(device)``: Powers off the device, the LEDs will turn off.

* ``setRGB(r: int, g: int, b: int, device)``: Sets the LED color configuration of the device to the r, g and b colors. (0-255)

* ``setWhite(intensity: int, device)``: Sets the device's LED to white with the specified intensiy. (0-255)

* ``setBuiltIn(mode: int, speed: int, device)``: Activates the selected predefined built-in mode at the selected speed (0-255). The built modes go from 37 to 56.

## Example use

The unittest code available in [tests/test.py](https://github.com/Aritzherrero4/python-trionesControl/blob/master/tests/test.py) can be used as a sample to use the available functions of the package. You can test your bulb / LED strip by using the following code too.

### Connect and power on the device

```python
import time
import trionesControl.trionesControl as tc

#Change the mac address to the one of your bulb or LED strip
device = tc.connect('00:00:00:00:00:00')
tc.powerOn(device)
```

### Change colors

```python
# RGB mode
tc.setRGB(100,100,100, device)
time.sleep(1)
tc.setRGB(255, 255, 255, device)
time.sleep(1)
tc.setRGB(255,0,0, device)
time.sleep(1)
tc.setRGB(0,255,0, device)

#White mode
time.sleep(10)
tc.setWhite(255, device)
```

### Built-in modes

```python
#Change built-in modes (37-56)
time.sleep(10)
tc.setBuiltIn(37, 1)
tc.time(10)
```

### Power off and disconnect

```python
tc.powerOff(device)
tc.disconnect(device)
```

## Licence

MIT Licence - Copyright 2020 Aritz Herrero

For more information, check [LICENCE](https://github.com/Aritzherrero4/python-trionesControl/blob/master/LICENSE) file.
