import base64
from io import BytesIO
from PIL import Image
import numpy as np
def encode_face_to_base64(face_array):
    # Pastikan array tidak kosong atau 1x1 pixel
    if face_array.shape[0] < 10 or face_array.shape[1] < 10:
        raise ValueError("Face crop too small")

    # Konversi ke uint8 jika masih float32
    if face_array.dtype != np.uint8:
        face_array = (face_array * 255).astype(np.uint8) if face_array.max() <= 1 else face_array.astype(np.uint8)

    img = Image.fromarray(face_array)
    buffer = BytesIO()
    img.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")