import cv2
import numpy as np
import time
import face_recognition

from database import create_database, save_log

from recognizer import load_known_faces, recognize_face

from config import CAMERA_INDEX, LOG_INTERVAL

def main():
    create_database()
    
    known_encodings, known_names = load_known_faces()
    
    if not known_encodings:
        print('No known faces found!')
        return
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print('Camera could not be opened!')
        return
    last_logged = {}
    print('Face Recognition Started!')
    
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print('Failed to capture frame')
                break
            rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            rgb = np.ascontiguousarray(rgb, dtype=np.uint8)
            
            face_locations = face_recognition.face_locations(rgb)
            face_encodings = face_recognition.face_encodings(rgb, face_locations)
            for location, encoding in zip(
                face_locations,
                face_encodings
            
            ):
                top, right, bottom, left = location
                name = recognize_face(encoding, known_encodings, known_names)
                if name != "Unknown":
                    current_time = time.monotonic()
                    pervious_time = last_logged.get(name, float('-inf'))
                    if current_time - pervious_time >= LOG_INTERVAL:
                        save_log(name)
                        last_logged[name] = current_time
                        
                        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
                    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                    cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            cv2.imshow('Face Recognition System', frame)
            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print('Face Recognition Stopped!')
if __name__ == "__main__":
    main()