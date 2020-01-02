#!/usr/bin/env python
import struct
import smbus
import sys
import time

def readVoltage(bus):
  "return voltage via smbus obj"
  address = 0x36
  read = bus.read_word_data(address,2)
  swapped = struct.unpack("<H",struct.pack(">H",read))[0]
  voltage = swapped * 1.25 /1000/16
  return voltage
  
def readCapacity(bus):
  address = 0x36
  read = bus.read_word_data(address,4)
  swapped = struct.unpack("<H",struct.pack(">H",read))[0]
  capacity = swapped/256
  return capacity
  
bus = smbus.SMBus(1)

while True:
  print "-----------"
  print "Voltage:%5.2fV" % readVoltage(bus)
  print "Battery:%5i%%" % readCapacity(bus)
  if readCapacity(bus) == 100:
    print "BATTERY FULL"
  if readCapacity(bus) < 20:
    print "***LOW BATTERY***"
  print "-----------"
  time.sleep(1)
