from pydantic import BaseModel
from typing import List, Optional

class FaceSaveCreate(BaseModel):
    name: Optional[str]
    face_embed: List[float]
