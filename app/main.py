from fastapi import APIRouter

app = APIRouter()


@app.get("/test")
async def tets():
    return {"message": "success"}

