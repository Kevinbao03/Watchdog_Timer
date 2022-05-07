import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(27, GPIO.OUT)

while True:
    GPIO.output(27, True)
    time.sleep(1.5)
    GPIO.output(27, False)





