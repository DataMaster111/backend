FROM python:3.11-slim-bullseye
RUN apt-get update
RUN apt-get install build-essential cmake -y
WORKDIR /usr/src/app

COPY requirements.txt .

ENV CMAKE_ARGS="-DCMAKE_CXX_FLAGS=-pthread"

# Прописать --no-cache-dir
RUN pip install -r requirements.txt

COPY ./app .

ENV PYTHONPATH=/usr/src/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]