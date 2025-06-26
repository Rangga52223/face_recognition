import numpy as np
from app.model.load_model import session
def get_embedding(preprocessed_face: np.ndarray) -> np.ndarray:
    """
    Input: preprocessed image (1, 3, 112, 112)
    Output: embedding (512,)
    """
    embedding = session.run(None, {"input.1": preprocessed_face})[0]
    return embedding[0]