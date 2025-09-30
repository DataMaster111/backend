import pandas as pd
from llama_cpp import Llama
from fastapi import APIRouter, UploadFile, HTTPException, status, Response, Request

from api.schemas import DBRequest

router = APIRouter()


@router.post("/load_files")
async def load_files(file: UploadFile, request: Request):
    format_file = file.filename.split('.')[-1].lower()
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
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"Error": "This format is not supported yet"})

    result = f"""
    Формат файла - {format_file}. 
    Количество записей в файле - {count_str}. 
    Немного записей для примера:
    {df.head(10).to_string()}"""
    user_prompt = f"""
        Ты - AI ассистент инженера данных. Я тебе даю информацию о файле, твоя задача проанализировать данные и ответить на вопросы без воды.

        ИНФОРМАЦИЯ О ФАЙЛЕ:
        {result}
        
        Проанализируй информацию о файле и ответь на следующие вопросы:
        1. В какой БД хранить (PostgreSQL, ClickHouse, HDFS)
        2. Как оптимизировать структуру
        3. Какие ETL-процессы предложить

        Ответь кратко на русском.
        """
    client = request.app.state.client
    if client is None:
        raise HTTPException(status_code=500, detail="AI model is not loaded yet")

    try:
        # Создание запроса к модели
        response = client.create_chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "Ты - эксперт по данным. Отвечай на русском."
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )
        recommendations = f"""Рекомендации ассистента: {response['choices'][0]['message']['content']}"""
        return Response(content=recommendations, media_type="text/plain")
    except Exception as e:
        raise HTTPException(500, f"AI model error: {str(e)}")


@router.post("/load_db")
async def load_db(connection_str: DBRequest):
    ...
