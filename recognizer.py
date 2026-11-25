import numpy as np
import face_recognition

from config import KNOWN_DIR, TOLERANCE

def load_known_faces():
    known_encodings = []
    
    known_names = []
    
    for image_path in KNOWN_DIR.iterdir():
        
        if image_path.suffix.lower() not in [
            ".jpg",
            ".jpeg",
            ".png"
        ]:
            continue
        try:
            print(f'Loading image: {image_path.name}')
            
            img = face_recognition.load_image_file(str(image_path), mode='RGB')
            img = np.asarray(img, dtype=np.uint8)
            img = np.ascontiguousarray(img)
            print('Image shape: ', img.shape)
            print('Image dtype: ', img.dtype)
            
            encodings = face_recognition.face_encodings(img)
            if not encodings:
                print(f'No face found: {image_path.name}')
                continue
            known_encodings.append(encodings[0])
            known_names.append(image_path.stem)
            print(f'Succuessfully loaded: {image_path.stem}')
        except Exception as error:
            print(f'Error loading {image_path.name}: {error}')
            continue
    return known_encodings, known_names

def recognize_face(encoding, known_encodings, known_names):
    if not known_encodings:
        return "Unknown"
    distances = face_recognition.face_distance(known_encodings, encoding)
    best_match_index = distances.argmin()
    if distances[best_match_index] <= TOLERANCE:
        return known_names[best_match_index]
    return "Unknown"