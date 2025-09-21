from fastapi import APIRouter, UploadFile

router = APIRouter()


@router.post("/load_files")
async def load_files(file: UploadFile):
    return file.filename

