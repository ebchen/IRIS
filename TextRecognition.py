from google.cloud import vision
from google.cloud.vision import types
#from autocorrect import spell
client = vision.ImageAnnotatorClient()
import io

#print("Processing Image...")

def recognizeImage(filename):
    with io.open(filename, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts

def findBiggestLbl(texts, indArray):
    maxLbl = ""
    maxInd = -1
    area = -1
    for t in range(len(texts)):
        yAr = abs((texts[t].bounding_poly.vertices[3].y)-(texts[t].bounding_poly.vertices[0].y))
        xAr = abs((texts[t].bounding_poly.vertices[2].x)-(texts[t].bounding_poly.vertices[0].x))
        currArea = yAr * xAr
        if currArea > area and t != 0 and t not in indArray:
            area = currArea
            maxLbl = texts[t].description
            maxInd = t
    print((maxLbl))
    return maxInd 

#lbls = recognizeImage("/home/pi/Desktop/iris/IMG_8130.JPG")
#indices = []
#for i in range(10):
    #indices.append(findBiggestLbl(lbls, indices))
