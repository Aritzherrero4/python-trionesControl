import pygatt
import logging
import pygatt.exceptions 
log = logging.getLogger(__name__)
def connect(MAC):
    try:
        adapter = pygatt.GATTToolBackend()
        adapter.start()
        device = adapter.connect(MAC)
    except pygatt.exceptions.NotConnectedError:
        raise pygatt.exceptions.NotConnectedError("Device nor connected!")
    log.info("Device connected")
    return device

def disconnect(device):
    try:
        device.disconnect()
    except pygatt.exceptions.NotConnectedError:
        raise pygatt.exceptions.NotConnectedError("Device nor connected!")
    log.info("Device disconnected")
def powerOn(device):
    try:
        device.char_write_handle(0x0009, b'\xcc\x23\x33')
    except pygatt.exceptions.NotConnectedError:
        raise pygatt.exceptions.NotConnectedError("Device nor connected!")
    log.info("Device powered on")

def powerOff(device):
    try:
        device.char_write_handle(0x0009, b'\xcc\x24\x33')
    except pygatt.exceptions.NotConnectedError:
        raise pygatt.exceptions.NotConnectedError("Device nor connected!")
    log.info("Device powered off")

def setRGB(r: int, g: int, b: int, device):
    # Values for color should be between 0 and 255
    if r > 255: r = 255
    if r < 0: r= 0
    if g > 255: g = 255 
    if g < 0: g = 0
    if b > 255: b = 255
    if b < 0: b = 0

    payload = bytearray() 
    payload.append(0x56)
    payload.append(r)
    payload.append(g)
    payload.append(b)
    payload.append(0x00)
    payload.append(0xF0)
    payload.append(0xAA)
    try:
        device.char_write_handle(0x0009, payload)
    except pygatt.exceptions.NotConnectedError:
        raise pygatt.exceptions.NotConnectedError("Device nor connected!")
    log.info("RGB set -- R: %d, G: %d, B: %d", r, g, b)

def setWhite(intensity: int, device):
    # Intensity value shoud be between 0  and 255
    if (intensity > 255): intensity = 255
    if (intensity < 0): intensity = 0
    payload = bytearray() 
    payload.append(0x56)
    payload.append(0x0)
    payload.append(0x0)
    payload.append(0x0)
    payload.append(intensity)
    payload.append(0x0F)
    payload.append(0xAA)
    try:
        device.char_write_handle(0x0009, payload)
    except pygatt.exceptions.NotConnectedError:
        raise pygatt.exceptions.NotConnectedError("Device nor connected!")
    log.info("White color set -- Intensity: %d", intensity)

def setBuiltIn(mode: int, speed: int, device):
    if mode<37 | mode > 56:
        raise pygatt.exceptions.BLEError("Invalid Mode")
    if speed<1: speed =1
    if speed > 255: speed = 255
    payload = bytearray() 
    payload.append(0xBB)
    payload.append(mode)
    payload.append(speed)
    payload.append(0x44)
    try:
        device.char_write_handle(0x0009, payload)
    except pygatt.exceptions.NotConnectedError:
        raise pygatt.exceptions.NotConnectedError("Device nor connected!")
    log.info("Default mode %d set -- Speed %d", mode, speed)

