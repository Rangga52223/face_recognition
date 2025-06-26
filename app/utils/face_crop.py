from facenet_pytorch import MTCNN as fcMtcNN
import cv2
import numpy as np

mtcnn = fcMtcNN(image_size=112, post_process=False, device='cpu')

def detect_and_align_face(img_rgb: np.ndarray) -> np.ndarray:
    """
    Input: img_rgb - RGB image (H, W, 3)
    Output: Aligned face image RGB [112,112,3] or None
    """
    face = mtcnn(img_rgb)
    if face is None:
        return None
    face = face.permute(1, 2, 0).numpy()  # convert to HWC
    return face

