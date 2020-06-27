import RPi.GPIO as GPIO
import time

terminal8 = 20

GPIO.setmode(GPIO.BOARD)
GPIO.setup(terminal8, GPIO.OUT)

GPIO.output(terminal8, GPIO.HIGH)
time.sleep(10)
GPIO.output(terminal8, GPIO.LOW)

GPIO.cleanup()
