import cv2
import os
import threading

# Set up camera
cap = cv2.VideoCapture(0)

# Create directory for dataset
dataset_dir = "dataset"
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# Get person's name
person_name = input("Enter person's name: ")

# Load face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Define function to capture images
def capture_images():
    # Set thread name
    threading.current_thread().name = "CaptureThread"

    # Capture images
    num_images = 10 # number of images to capture
    for i in range(num_images):
        # Capture frame from camera
        ret, frame = cap.read()

        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        # Save image if face is detected
        if len(faces) == 1:
            # Crop image to face
            (x, y, w, h) = faces[0]
            crop_img = frame[y:y+h, x:x+w]

            # Resize image to 128x128
            resized_img = cv2.resize(crop_img, (128, 128))

            # Save image
            image_path = os.path.join(dataset_dir, person_name + "_" + str(i) + ".jpg")
            cv2.imwrite(image_path, resized_img)

        # Wait for key press to capture next image
        cv2.waitKey(2000)

    print("Image capture complete")

# Create thread to capture images
t = threading.Thread(target=capture_images)
t.start()

# Display captured frames in main thread
while t.is_alive():
    ret, frame = cap.read()
    cv2.imshow('Capturing...', frame)
    cv2.waitKey(1)

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
