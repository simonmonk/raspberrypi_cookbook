import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

input_A = 18
input_B = 23

GPIO.setup(input_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(input_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

a = True
b = True

while True:
    new_a = GPIO.input(input_A)
    new_b = GPIO.input(input_B)
    if new_a != a or new_b != b :
        print('a=' + str(a) + ' b=' + str(b))
        a, b = new_a, new_b