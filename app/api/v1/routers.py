import pandas as pd
from openai import OpenAI
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
    user_prompt = f"""
        Ты - AI ассистент инженера данных. Проанализируй этот файл:

        ИНФОРМАЦИЯ О ФАЙЛЕ:
        {Response(content=result, media_type="text/plain")}

        Дай рекомендации по:
        1. В какой БД хранить (PostgreSQL, ClickHouse, HDFS)
        2. Как оптимизировать структуру
        3. Какие ETL-процессы предложить

        Ответь кратко на русском.
        """
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
    )

    # Создание запроса к модели
    response = client.chat.completions.create(
        model="yandex/YandexGPT-5-Lite-8B-instruct-GGUF",
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
    recomindations = f"""Рекомендации ассистента: {response.choices[0].message.content}"""
    return Response(content=recomindations, media_type="text/plain")

@router.post("/load_db")
async def load_db(connection_str: DBRequest):
    ...