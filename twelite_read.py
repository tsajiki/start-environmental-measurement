#!/usr/bin/python
# coding: UTF-8

from serial import *
from sys import exit
import csv
import datetime

# シリアルポートを開く（"COM5"の場合）
try:
    ser = Serial("COM5", 115200)
    print("open serial port: %s" % "COM5")
except:
    print("cannot open serial port: %s" % "COM5")
    exit(1)

# データを１行ずつ解釈する
while True:
    now = datetime.datetime.now()
    now=now.isoformat()

    date = datetime.datetime.today()
    date=date.isoformat()

    line = ser.readline().rstrip() # １ライン単位で読み出し、末尾の改行コードを削除（ブロッキング読み出し）

    strLine=line.decode()
    arrLine=strLine.split(";")
    arrLine[0]=now

    print(arrLine)
    if len(arrLine) > 4 and (arrLine[11]=='B' or arrLine[11]=='T'):
        #print(arrLine[7] + " " + arrLine[8] + " " + arrLine[12])
        # ファイル名を日付にしたい
        with open('names1.csv', 'a', newline='', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(arrLine)
