from google.cloud import vision
from google.cloud.vision import types
client = vision.ImageAnnotatorClient()
import io

print("Processing Image...")

def recognizeImage(filename):
    with io.open(filename, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    responseWeb = client.web_detection(image=image)
    annotations = responseWeb.web_detection
    if annotations.web_entities:
        for entity in annotations.web_entities:
            print(entity.description)
    return annotations.web_entities

def chooseBill(label):
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

labels = recognizeImage("/home/pi/Desktop/iris/try.jpg")
value = -1
for lbl in labels:
    val = chooseBill(str(lbl))
    if val > 0:
        value = val
        print(str(lbl))
        break

print(value)
