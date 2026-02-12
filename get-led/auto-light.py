import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

state = 0


photo_tr = 6
GPIO.setup(photo_tr, GPIO.IN)


period = 1.0
while True:
    if not GRIO.input(photo_tr):
        state = not state
        GPIO.output(led, state)
        time.sleep(period)