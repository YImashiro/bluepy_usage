#!/usr/bin/env python3
"""execute with sudo"""
from bluepy.btle import Scanner

scanner = Scanner()
i= 0

for scanned in scanner.scan(timeout=5):
    i+=1
    print("{}.".format(i))
    print("Local Name  : {}".format(scanned.getValueText(9)))
    print("MacAddress  : {}".format(scanned.addr))
    print("AddressType : {}".format(scanned.addrType))
    print("ALL GAP DATA ARE AS FOLLOWS")
    for tuple in scanned.getScanData():
        adtype, description, value = tuple[0], tuple[1], tuple[2]
        print()
        print("adtype      : {:<3}".format(tuple[0]))
        print("description : {:<15}".format(tuple[1]))
        print("value       : {:<20}".format(tuple[2]))
    print()
    print()
    

