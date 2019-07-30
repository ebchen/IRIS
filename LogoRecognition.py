from google.cloud import vision
from google.cloud.vision import types
client = vision.ImageAnnotatorClient()
import io

#print("Processing Image...")

def recognizeLogos(filename):
    with io.open(filename, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    for logo in logos:
        print(logo.description)
    return logos

#recognizeLogos("/Users/sameer/Desktop/Iris/images/IMG_8139.JPG")


