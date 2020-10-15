import pygatt
def connect(MAC):
    try:
        adapter = pygatt.GATTToolBackend()
        adapter.start()
        device = adapter.connect(MAC)
    finally:
        return device
def disconnect(device):
    device.disconnect()

def powerOn(device):
    a = device.char_write_handle(0x0009, b'\xcc\x23\x33')

def powerOff(device):
    a = device.char_write_handle(0x0009, b'\xcc\x24\x33')

def setRGB(r: int, g: int, b: int, device):
    payload = bytearray() 
    payload.append(0x56)
    payload.append(r)
    payload.append(g)
    payload.append(b)
    payload.append(0x00)
    payload.append(0xF0)
    payload.append(0xAA)
    a = device.char_write_handle(0x0009, payload)
  
