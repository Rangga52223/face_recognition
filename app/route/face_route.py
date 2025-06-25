from app.route import *

@router.get("/")
async def get_all_faceroute():
    return get_all_face()

@router.post("/register")
async def register_face(name: str = Form(...), file: UploadFile = File(...)):
    try:
        if not file or not name:
            raise HTTPException(status_code=400, detail="File and name are required")
        content = await file.read()
        return register_face_re(name, content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/recognition")
async def register_face(file: UploadFile = File(...)):
    try:
        if not file :
            raise HTTPException(status_code=400, detail="File and name are required")
        content = await file.read()
        return recognition_face_re(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/delete/{ids}")
async def delete_face(ids: str):
    try:
        if not ids:
            return HTTPException(status_code=400, detail="ID is required")
        return delete_face_re(ids)
    except :
        raise HTTPException(status_code=400, detail="ID is required")


