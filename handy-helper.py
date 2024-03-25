import RPi.GPIO as GPIO
import time

# Based on code from https://projects.raspberrypi.org/en/projects/grandpa-scarer/3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

pwm = GPIO.PWM(11, 50)
pwm.start(0) 
time.sleep(0.5)
 
for i in range(5):
    pwm.ChangeDutyCycle(1)
    time.sleep(0.07)
    pwm.ChangeDutyCycle(0)
    time.sleep(0.4)
time.sleep(1)
pwm.ChangeDutyCycle(10)
time.sleep(0.5)
 
pwm.stop()
GPIO.cleanup()
