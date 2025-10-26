from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(version="0.1.0")


@app.get('/')
async def index():
    return {'response': 'This is a FastApi backend app'}


# Установка favicon
@app.get("/favicon.ico")
async def read_favicon():
    return FileResponse("src/static/favicon.ico")