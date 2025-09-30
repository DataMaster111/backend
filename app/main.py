from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from llama_cpp import Llama

from api.v1 import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Start")
    app.state.client = Llama(model_path="./model/YandexGPT-5-Lite-8B-instruct-Q4_K_M.gguf", verbose=False)
    print("End")
    yield
        #if app.state.client:
            #del app.state.client


app = FastAPI(lifespan=lifespan)
app.include_router(router=router)

@app.get("/test")
async def tets():
    return {"message": "success"}

