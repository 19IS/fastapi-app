import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.routers import news
from src.settings import (
    STATIC_FILES_DIR,
    TEMPLATES_DIR,
    FASTAPI_HOST,
    FASTAPI_PORT
)

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(
    news.router, tags=['News'], prefix='/api/database/news'
)

app.mount(
    path="/static",
    app=StaticFiles(directory=STATIC_FILES_DIR),
    name='static'
)

templates = Jinja2Templates(
    directory=TEMPLATES_DIR
)


@app.get('/api/healthchecker')
def root():
    return {
        'status': 'success',
        'message': 'Добро пожаловать в сервер FastAPI + MongoDB'
    }


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={
            'request': request,
            'title': 'Главная страница',
        }
    )


@app.get('/about')
def about(request: Request):
    return templates.TemplateResponse(
        name="about.html",
        context={
            'request': request,
            'title': 'О приложении',
        }
    )


if __name__ == '__main__':
    uvicorn.run(
        "src.main:app",
        host=FASTAPI_HOST,
        port=FASTAPI_PORT,
    )
