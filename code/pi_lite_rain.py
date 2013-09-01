import serial
import random

ser = serial.Serial('/dev/ttyAMA0', 9600)

while True:
    col = random.randint(1, 14)
    row = random.randint(1, 9)
    ser.write("$$$P%d,%d,TOGGLE\r" % (col, row))

