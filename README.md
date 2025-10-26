# Auth server

## 


- Подключаем интерпритатор: 

```sh
source .venv/bin/activate
pip install poetry
poetry init --name "kek-auth"
```

```sh
mkdir -p src/app
```

cat <<EOF > ./src/app/main.py
"from fastapi import FastAPI

app = FastAPI(version="0.1.0")


@app.get('/')
async def index():
    return {'response': 'This is a FastApi backend app'}
EOF"


```sh
poetry add fastapi
poetry add uvicorn
```

### add favicon

- create static directory:
```sh
mkdir -p src/static
```
- copy `favicon.ico` to `src/static` 

- add some changes to `main.py`:
```python
...
from fastapi.responses import FileResponse
...

# Установка favicon
@app.get("/favicon.ico")
async def read_favicon():
    return FileResponse("src/static/favicon.ico")
```