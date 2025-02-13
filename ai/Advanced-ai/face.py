import cv2
import numpy as np
import os

# path to the folder containing your face images
face_images_path = 'path_to_folder_containing_face_images'

# create a face recognition model
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# load the face images and train the model
face_images = []
face_labels = []
for filename in os.listdir(face_images_path):
    if filename.endswith('.jpg'):
        image = cv2.imread(os.path.join(face_images_path, filename), cv2.IMREAD_GRAYSCALE)
        face_images.append(image)
        face_labels.append(1) # or any label you want to use for your face
face_recognizer.train(face_images, np.array(face_labels))

# create a video capture object
cap = cv2.VideoCapture(0)

# create a face detection cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # read a frame from the video stream
    ret, frame = cap.read()

    # convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the frame using the cascade classifier
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # for each face detected, recognize it using the face recognition model
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        label, confidence = face_recognizer.predict(roi_gray)

        # if the recognized face is your face, draw a green rectangle around it
        if label == 1 and confidence < 100:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    
    # display the frame with the detected faces
    cv2.imshow('Face Detection', frame)

    # if the 'q' key is pressed, exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()