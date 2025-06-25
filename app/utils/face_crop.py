from mtcnn import MTCNN as MtCnn
from facenet_pytorch import MTCNN as fcMtcNN
import cv2
import numpy as np

mtcnn = fcMtcNN(image_size=112, post_process=True, device='cpu')

def detect_face(image: np.ndarray):
    detector = MtCnn()
    results = detector.detect_faces(image)
    if not results:
        return None  
    face = results[0]['box']
    x, y, w, h = face
    return (x, y, w, h)

def detect_and_align_face(img_rgb: np.ndarray):
    face = mtcnn(img_rgb)
    if face is None:
        return None
    face = face.permute(1, 2, 0).numpy()
    return face