#!/usr/bin/env python3
"""execute with sudo"""

from bluepy.btle import DefaultDelegate
from bluepy.btle import Peripheral
from bluepy import btle

class MyDelegate(btle.DefaultDelegate):
    """Class for handle Notification"""
    def __init__(self):
        super().__init__()

    def handleNotification(self,cHandle,data):
        """Called when waitForNotification method returns True.
        Write what you want to do when notification is called."""
        print(data)


def enableNotification(handle):
    """If you want to use Notification, you need to write \x01\x00 to Descriptor.
    'Descriptor handle' equals 'value handle' + 1.
    if you want to use this function,input value handle to argument"""
    peripheral.writeCharacteristic(handle+1,(1).to_bytes(2, byteorder='little'))
    while True:
        if peripheral.waitForNotifications(handle):
            continue
        break
        
'''Make peripheral object. 
Change first argument:"MacAddress" to a peripheral MacAddress.
Second argument is "btle.ADDR_TYPE_RANDOM" or btle.ADDR_TYPE_PUBLIC"
By getAddr.py shows these information.
If you use this program, delete # and comment out
peripheral= Peripheral("d8:e3:66:b3:b9:95",btle.ADDR_TYPE_RANDOM)
'''
#peripheral = Peripheral("MacAddress",btle.ADDR_TYPE_"RANDOM/PUBLIC")
peripheral = Peripheral("d8:e3:66:b3:b9:95",btle.ADDR_TYPE_RANDOM)

'''show structure of GATT Service'''
for srv in peripheral.getServices():
    print(srv)
    for characteristic in srv.getCharacteristics():
        print(characteristic)

#instanciate Delegate object
delegate = MyDelegate()
peripheral.withDelegate(delegate)

#To get notification,you need to do this function
handle = 11
enableNotification(handle)

print("disconnected")
peripheral.disconnect()




    
