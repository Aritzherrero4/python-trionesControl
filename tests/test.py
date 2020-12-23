import time
from trionesControl import trionesControl as tc
import logging
import unittest

#Set the MAC address of the lights before executing
device = tc.connect('00:00:00:00:00:00') 
chars = device.discover_characteristics()


log = logging.getLogger(__name__)
logging.basicConfig(level=20)

class fullTestCase(unittest.TestCase):
    def powerOn(self):
        tc.powerOn(device)
        
    def colorChange(self):
        tc.setRGB(100,100,100, device)
        time.sleep(1)
        tc.setRGB(255, 255, 255, device)
        time.sleep(1)
        tc.setRGB(255,0,0, device)
        time.sleep(1)
        tc.setRGB(0,255,0, device)
        time.sleep(1)
        tc.setRGB(0,0,255, device)
        time.sleep(1)
        tc.setRGB(0,0,255, device)
        time.sleep(1)
        tc.setRGB(150,0,150, device)
        time.sleep(2)

    def setWhite(self):
        tc.setWhite(255, device)
        time.sleep(10)

    def builtIn(self):
        tc.setBuiltIn(37, 1, device)
        time.sleep(10)

    def powerOff(self):
        time.sleep(10)
        tc.powerOff(device)
        tc.disconnect(device)
    
    def testLights(self):
        self.powerOn()
        self.colorChange()
        self.setWhite()
        self.builtIn()
        self.powerOff()

if __name__ == '__main__':
    unittest.main()