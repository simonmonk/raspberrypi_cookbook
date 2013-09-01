import RPi.GPIO as GPIO
import time

enable_pin = 18
in1_pin = 23
in2_pin =24

GPIO.setmode(GPIO.BCM)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)

pwm = GPIO.PWM(enable_pin, 500)
pwm.start(0)

def clockwise():
    GPIO.output(in1_pin, True)    
    GPIO.output(in2_pin, False)
 
def counter_clockwise():
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin, True)
 
while True:
    cmd = raw_input("Command, f/r 0..9, E.g. f5 :")
    direction = cmd[0]
    if direction == "f":
        clockwise()
    else: 
        counter_clockwise()
    speed = int(cmd[1]) * 10
    pwm.ChangeDutyCycle(speed)

