import cv2
import numpy as np
import os

if not os.path.exists("dataset"):
    os.mkdir("dataset")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def capture_faces(user_id):
    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face = gray[y:y+h, x:x+w]
            cv2.imwrite(f"dataset/User.{user_id}.{count}.jpg", face)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Capturing Faces", frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
            break

    cap.release()
    cv2.destroyAllWindows()

def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces, ids = [], []

    for file in os.listdir("dataset"):
        img = cv2.imread(f"dataset/{file}", cv2.IMREAD_GRAYSCALE)
        faces.append(np.array(img, dtype=np.uint8))
        ids.append(int(file.split(".")[1]))  

    recognizer.train(faces, np.array(ids))
    recognizer.save("face_model.yml")

def recognize_faces():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("face_model.yml")

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        user_count = 1 

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            label, confidence = recognizer.predict(face)

            user_label = f"User {user_count}" if confidence < 100 else "Unknown"
            user_count += 1 

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, user_label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

capture_faces(user_id=1) 
train_model()
recognize_faces()
