import cv2
import numpy as np
import os
import re

path = "C:/Users/adica/self_projects/CCC/ai/Advanced-A.I-code-Jarvis-not-finished-main/samples"

recognizer = cv2.face.LBPHFaceRecognizer_create()
cascPath = os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
FaceCascade = cv2.CascadeClassifier(cascPath)

def Images_And_Labels(path):
    ImagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    
    for ImagePath in ImagePaths:
        # Get the ID from the file name using regular expressions to match numeric characters
        id = int(re.search(r'\d+', os.path.split(ImagePath)[-1]).group(0))
    
        # Load the image and detect faces
        img = cv2.imread(ImagePath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = FaceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    
        # Add face samples and IDs to lists
        for (x,y,w,h) in faces:
            faceSamples.append(gray[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print("Training faces, It will take a few seconds. Wait...")

# Train for 1000 epochs
for i in range(1000):
    faces, ids = Images_And_Labels(path)
    recognizer.train(faces, np.array(ids))

    # Print progress every 100 epochs
    if i % 100 == 0:
        print("Epoch {} completed".format(i))

recognizer.write('C:/Users/adica/self_projects/CCC/ai/Advanced-A.I-code-Jarvis-not-finished-main/trainer/trainer.yml')

print("Model trained, Now we can recognize your face")
