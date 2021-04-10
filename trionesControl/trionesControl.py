import pygatt
import logging
import pygatt.exceptions 

MAIN_CHARACTERISTIC_UUID = "0000ffd9-0000-1000-8000-00805f9b34fb"

log = logging.getLogger(__name__)

def connect(MAC, reset_on_start=True):
    """
    Create and start a new backend adapter and connect it to a device.

    When connecting to multiple devices at the same time make sure to set reset_on_start
    to False after the first connection is made, otherwise all connections made before are
    invalidated.

    :param string MAC: MAC address of the device to connect to.
    :param bool reset_on_start: Perhaps due to a bug in gatttol or pygatt,
        but if the bluez backend isn't restarted, it can sometimes lock up
        the computer when trying to make a connection to HCI device.
    """
    try:
        adapter = pygatt.GATTToolBackend()
        adapter.start(reset_on_start=reset_on_start)
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

def powerOn(device, wait_for_response=False):
    """
    :param bool wait_for_response: wait for response after writing. A GATT "command"
    is used when not waiting for a response. The remote host will not
    acknowledge the write.
    """

    try:
        device.char_write(MAIN_CHARACTERISTIC_UUID, b'\xcc\x23\x33', wait_for_response=wait_for_response)
    except pygatt.exceptions.NotConnectedError:
        raise pygatt.exceptions.NotConnectedError("Device nor connected!")
    log.info("Device powered on")

def powerOff(device, wait_for_response=False):
    """
    :param bool wait_for_response: wait for response after writing. A GATT "command"
    is used when not waiting for a response. The remote host will not
    acknowledge the write.
    """

    try:
        device.char_write(MAIN_CHARACTERISTIC_UUID, b'\xcc\x24\x33', wait_for_response=wait_for_response)
    except pygatt.exceptions.NotConnectedError:
        raise pygatt.exceptions.NotConnectedError("Device nor connected!")
    log.info("Device powered off")

def setRGB(r: int, g: int, b: int, device, wait_for_response=False):
    """
    :param bool wait_for_response: wait for response after writing. A GATT "command"
    is used when not waiting for a response. The remote host will not
    acknowledge the write.
    """
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
        device.char_write(MAIN_CHARACTERISTIC_UUID, payload, wait_for_response=wait_for_response)
    except pygatt.exceptions.NotConnectedError:
        raise pygatt.exceptions.NotConnectedError("Device nor connected!")
    log.info("RGB set -- R: %d, G: %d, B: %d", r, g, b)

def setWhite(intensity: int, device, wait_for_response=False):
    """
    :param bool wait_for_response: wait for response after writing. A GATT "command"
    is used when not waiting for a response. The remote host will not
    acknowledge the write.
    """
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
        device.char_write(MAIN_CHARACTERISTIC_UUID, payload, wait_for_response=wait_for_response)
    except pygatt.exceptions.NotConnectedError:
        raise pygatt.exceptions.NotConnectedError("Device nor connected!")
    log.info("White color set -- Intensity: %d", intensity)

def setBuiltIn(mode: int, speed: int, device, wait_for_response=False):
    """
    :param bool wait_for_response: wait for response after writing. A GATT "command"
    is used when not waiting for a response. The remote host will not
    acknowledge the write.
    """

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
        device.char_write(MAIN_CHARACTERISTIC_UUID, payload, wait_for_response=wait_for_response)
    except pygatt.exceptions.NotConnectedError:
        raise pygatt.exceptions.NotConnectedError("Device nor connected!")
    log.info("Default mode %d set -- Speed %d", mode, speed)

