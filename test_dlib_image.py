import face_recognition
import numpy as np

image = face_recognition.load_image_file('known/erfan.jpg.jpg', mode='RGB')

image = np.array(image, dtype=np.uint8, order='C', copy=True)

print('Shape:', image.shape)
print('Dtype:', image.dtype)

locations = face_recognition.face_locations(image)

print('Face locations: ', locations)