import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
capteur = 7

GPIO.setup(capteur, GPIO.IN)

print ('xxx')
time.sleep(2)

print ('ready !')

while True:
    if GPIO.input(capteur):
        print('VUEEEE')
        time.sleep(2)
    time.sleep(0.1)