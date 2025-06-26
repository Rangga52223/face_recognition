from facenet_pytorch import MTCNN as fcMtcNN
import cv2
import numpy as np

mtcnn = fcMtcNN(image_size=112, post_process=False, device='cpu')

def detect_and_align_face(img_rgb: np.ndarray):
    print('DEBUG: detect')
    face = mtcnn(img_rgb)  # Output: Tensor [3, 112, 112]
    if face is None:
        return None
    face = face.permute(1, 2, 0).cpu().numpy()  # Convert to [112,112,3]
    return face

