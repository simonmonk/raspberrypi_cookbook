import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin_1 = 18
led_pin_2 = 23
led_pin_3 = 24
switch_pin = 25

GPIO.setup(led_pin_1, GPIO.OUT)
GPIO.setup(led_pin_2, GPIO.OUT)
GPIO.setup(led_pin_3, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
GPIO.output(led_pin_1, 1)
time.sleep(1)
GPIO.output(led_pin_2, 1)
time.sleep(1)
GPIO.output(led_pin_3, 1)
time.sleep(1)
GPIO.output(led_pin_1, 0)
time.sleep(1)
GPIO.output(led_pin_2, 0)
time.sleep(1)
GPIO.output(led_pin_3, 0)
time.sleep(1)

while True:
    print(GPIO.input(switch_pin))
    time.sleep(1)