from fastapi import APIRouter, UploadFile

from api.schemas import DBRequest

router = APIRouter()


@router.post("/load_files")
async def load_files(file: UploadFile):
    return file.filename


@router.post("/load_db")
async def load_db(connection_str: DBRequest):
    ...