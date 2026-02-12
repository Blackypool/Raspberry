#модули времени и работы с GPIO
import RPi.GPIO as GPIO
import time

#режим GPIO.BCM обращения к GPIO пинам
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setmode(GPIO.BCM)

#переменная с номером GPIO-пина
led = 26

#GPIO26, как цифровой выход
GPIO.setup(led, GPIO.OUT)

#состояние светодиода
state = 0

#период мигания в секундах
period = 1.0

while True:
    GPIO.output(led, state)
    state = not state
    time.sleep(period)
    period = period * 0.8