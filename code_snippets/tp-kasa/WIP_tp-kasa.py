'''
https://python-kasa.readthedocs.io/en/latest/index.html

```bash
pip install python-kasa
kasa discover
```
DeprecationWarning: SmartPlug is deprecated, use IotPlug from package kasa.iot 
instead or use Discover.discover_single() and Device.connect() to support 
new protocols

from kasa import Discover, SmartPlug

WORK IN PROGRESS
'''


import asyncio
from kasa import Discover
from kasa.iot import IotDevice

async def main():
    # Discover devices on the network
    devices = await Discover.discover()
    
    if not devices:
        print("No devices found")
        return
    
    # Get the first device found
    addr, dev = next(iter(devices.items()))
    print(f"Found device at {addr}")
    
    # Connect to the device
    device = IotDevice(addr)
    await device.connect()
    
    # Update the device state
    await device.update()
    print(f"Current state: {device.state}")
    
    # Turn the plug on
    await device.turn_on()
    print("Turned on")
    
    # Wait for a few seconds
    await asyncio.sleep(5)
    
    # Turn the plug off
    await device.turn_off()
    print("Turned off")

# Run the main function
asyncio.run(main())