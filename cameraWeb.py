#!/usr/bin/python  
from picamera import PiCamera
import time  
import RPi.GPIO as GPIO 
import WebRecognition
print("Imported libraries")



filepath = '/home/pi/Desktop/iris/image0.jpg'

GPIO.setmode(GPIO.BOARD) 
  
def RCtime (RCpin):  
        reading = 0  
        GPIO.setup(RCpin, GPIO.OUT)  
        GPIO.output(RCpin, GPIO.LOW)  
        time.sleep(0.1)  
  
        GPIO.setup(RCpin, GPIO.IN)  
        while (GPIO.input(RCpin) == GPIO.LOW):  
                reading += 1  
        return reading
    
camera = PiCamera()
print("Initialized camera")
camera.stop_preview()
camera.start_preview()
print("Started camera preview")
camera.resolution =(1920, 1024)

while True:
    if (RCtime(11) > 15000):
        camera.capture(filepath)
        print("Captured Image")
        camera.stop_preview()
        print("Processing Image...")
        lbls = WebRecognition.recognizeImage(filepath)
        time.sleep(10)


