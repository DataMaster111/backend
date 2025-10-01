from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from llama_cpp import Llama

from api.v1 import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.client = Llama(model_path="./model/YandexGPT-5-Lite-8B-instruct-Q4_K_M.gguf", verbose=False)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=router)
