#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
from datetime import time
import io

kapcs = serial.Serial(
    port='COM3',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout= 1,
    xonxoff= True
    
)

try:
    kapcs.isOpen()
except:
    print('Port nyitasa')
    kapcs.open()
    kapcs.isOpen()
#kapcs.close()
#kapcs.open()
#kapcs.isOpen()
serial.win

print 'Serial port kapcsolodas kesz \r\n Kilepeshez ird be "exit"'

adat=1

while 1:
    #bevitel billentyűzettel
    adat = raw_input(">> ")

    if adat == 'exit':
        kapcs.close()
        exit()
    else:
        # küldés eszköz felé
        # \r\n sortörés
        #kapcs.write(adat + '\r\n' + '!')
        kapcs.write(adat)
        # kapcs.flushInput()
        # kapcs.flushOutput()
        # kimenet=''
        # while True:
        #     kimenet += kapcs.readline()
        #     print kimenet
        #
        # if kimenet != "":
        #     print ">>"
        kimenet=''
        time.sleep(1) # 1 másodperc várakozás kimenet olvasása előtt
        print adat
        print kapcs.inWaiting()
        while kapcs.inWaiting() > 0:
            print kapcs.inWaiting()
            kimenet += kapcs.readline()
        #if kimenet != '':
        print ">>" + kimenet