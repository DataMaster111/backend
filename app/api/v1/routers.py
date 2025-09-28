import pandas as pd

from fastapi import APIRouter, UploadFile, HTTPException, status, Response

from api.schemas import DBRequest

router = APIRouter()


@router.post("/load_files")
async def load_files(file: UploadFile):
    format_file = file.filename.split('.')[-1]
    if format_file == "csv":
        df = pd.read_csv(file.file)
        count_str = df.shape[0]
    elif format_file == "json":
        df = pd.read_json(file.file)
        count_str = df.shape[0]
    elif format_file == "xml":
        df = pd.read_xml(file.file)
        count_str = df.shape[0]
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"Error": "This format is not supported yet"})

    result = f"""
    Формат файла - {format_file}. 
    Количество записей в файле - {count_str}. 
    Немного записей для примера:
    {df.head(20).to_string()}"""

    return Response(content=result, media_type="text/plain")


@router.post("/load_db")
async def load_db(connection_str: DBRequest):
    ...