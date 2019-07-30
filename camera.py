#!/usr/bin/python  
from picamera import PiCamera
import time  
import RPi.GPIO as GPIO
from WebRecognition import recognizeImage
import TextRecognition
from gtts import gTTS
import pygame
from LogoRecognition import recognizeLogos
print("Imported libraries")

isMoney = False

filepath = '/home/pi/Desktop/iris/image0.jpg'
audioPath = '/home/pi/Desktop/iris/image0.mp3'

GPIO.setmode(GPIO.BOARD)

pygame.mixer.init()
  
def RCtime (RCpin):  
        reading = 0  
        GPIO.setup(RCpin, GPIO.OUT)  
        GPIO.output(RCpin, GPIO.LOW)  
        time.sleep(0.1)  
  
        GPIO.setup(RCpin, GPIO.IN)  
        while (GPIO.input(RCpin) == GPIO.LOW):  
                reading += 1  
        return reading
    

def findBill(label):
    if label.find('bill') != -1:
        if label.find('one') != -1:
          return 1
        elif label.find('two') != -1:
          return 2
        elif label.find('five') != -1:
          return 5
        elif label.find('ten') != -1:
          return 10
        elif label.find('twenty') != -1:
          return 20
        elif label.find('fifty') != -1:
          return 50
        elif label.find('hundred') != -1:
          return 100
    return -1
    
camera = PiCamera()
camera.rotation = 270
print("Initialized camera")
camera.stop_preview()
camera.start_preview()
print("Started camera preview")
camera.resolution =(1920, 1024)

while True:
    isMoney = False
    if (RCtime(11) > 10000):
        camera.capture(filepath)
        print("Captured Image")
        camera.stop_preview()
        print("Processing Image...")
        pygame.mixer.music.load("/home/pi/Desktop/iris/step1.mp3")
        pygame.mixer.music.play()
        webLbls = recognizeImage(filepath)
        endStr = "We found: "
        for entity in webLbls:
            val = findBill(entity.description)
            if (val > 0):
                isMoney = True
                endStr = "Dollar value is " + str(val)
                break
        pygame.mixer.music.load("/home/pi/Desktop/iris/step2.mp3")
        pygame.mixer.music.play()
        if (isMoney != True):
            lbls = TextRecognition.recognizeImage(filepath)
            indices = []
            if (len(lbls) > 0):
                for i in range(5):
                    indices.append(TextRecognition.findBiggestLbl(lbls, indices))
                for ind in indices:
                    endStr += str(lbls[ind].description)
                    endStr += " "
                pygame.mixer.music.load("/home/pi/Desktop/iris/step3.mp3")
                pygame.mixer.music.play()
            logos = recognizeLogos(filepath) 
            if len(logos) > 0:
                print("Logo found: " + str(logos[0].description))
                endStr += str(logos[0].description)
            pygame.mixer.music.load("/home/pi/Desktop/iris/step4.mp3")
            pygame.mixer.music.play()
        print(endStr)
        tts = gTTS(text=endStr, lang='en')
        tts.save(audioPath)
        pygame.mixer.music.load(audioPath)
        pygame.mixer.music.play()
        time.sleep(10)

