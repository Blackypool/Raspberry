import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

#up_up_up
upper = 9
GPIO.setup(upper, GPIO.IN)

#down_down_down
downer = 10
GPIO.setup(downer, GPIO.IN)

num = 0             # up_or_down?
sleep_time = 0.2    # sleep

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    if GPIO.input(upper):
    num = num + 1
    print(num, dec2bin(num))
    time.sleep(sleep_time)

    if GPIO.input(downer):
    num = num - 1
    print(num, dec2bin(num))
    time.sleep(sleep_time)

    GPIO.output(leds, dec2bin(num))