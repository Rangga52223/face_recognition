import cv2
import numpy as np
def preprocess_face(img: np.ndarray, bbox: tuple) -> np.ndarray:
    """
    img: original BGR image (OpenCV)
    bbox: (x, y, w, h) tuple
    return: RGB image [112,112,3] float32 normalized
    """
    x, y, w, h = bbox
    face = img[y:y+h, x:x+w]  # crop
    face = cv2.resize(face, (112, 112))
    face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)  # Convert to RGB
    face = face.astype(np.float32)
    face = (face / 255.0 - 0.5) / 0.5  # Normalisasi ke [-1, 1]
    return face