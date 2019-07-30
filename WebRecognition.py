from google.cloud import vision
from google.cloud.vision import types
client = vision.ImageAnnotatorClient()
import io

#print("Processing Image...")

def recognizeImage(filename):
    with io.open(filename, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    responseWeb = client.web_detection(image=image)
    annotations = responseWeb.web_detection
    return annotations.web_entities

#recognizeImage("/home/pi/Desktop/iris/image0.jpg")
