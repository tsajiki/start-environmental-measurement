#!/usr/bin/python
# coding: UTF-8

from serial import *
from sys import exit
import csv
import datetime

# open serial port: "COM5" etc
try:
    ser = Serial("COM5", 115200)
    print("open serial port: %s" % "COM5")
except:
    print("cannot open serial port: %s" % "COM5")
    exit(1)

while True:
    now = datetime.datetime.now()
    today = now.date()
    now = now.isoformat()

    line = ser.readline().rstrip()
    strLine = line.decode()
    arrLine = strLine.split(";")
    arrLine[0] = now
    print(arrLine)

    if len(arrLine) > 4 and (arrLine[11] == 'B' or arrLine[11] == 'T'):
        #print(arrLine[7] + " " + arrLine[8] + " " + arrLine[12])

        fileName = '{}.csv'.format(today)
        with open(fileName, 'a', newline='', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(arrLine)
