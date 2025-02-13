import cv2
import os

def capture_faces(name, num_photos=10, output_dir='faces'):
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    count = 0

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_dir = os.path.join(output_dir, name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    while count < num_photos:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count += 1
            face_img = gray[y:y+h, x:x+w]
            file_name = os.path.join(output_dir, f'{name}_{count}.jpg')
            cv2.imwrite(file_name, face_img)
            print(f'Image saved as {file_name}')

        cv2.imshow('Capturing Faces', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    name = input('Enter the name of the person: ')
    num_photos = int(input('Enter the number of photos to capture: '))
    output_dir = 'C:/Users/adica/OneDrive/Pictures/test photos'
    capture_faces(name, num_photos, output_dir)