import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
state = 0
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 200) # where + 1/T
duty = 0.0               # start
pwm.start(duty)          # strat pwd ot duty

while True:
    pwm.ChangeDutyCycle(duty) # update duty
    time.sleep(0.05)
    
    duty += 1.0
    if duty > 100.0:
        duty = 0.0