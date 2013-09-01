import serial

ser = serial.Serial('/dev/ttyAMA0', 9600)

while True:
    message = raw_input("Enter message: ")
    ser.write(message)
