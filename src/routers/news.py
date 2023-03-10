from datetime import datetime
from fastapi import HTTPException, status, APIRouter, Response

from pymongo.collection import ReturnDocument
from src.database import News
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError
from src.serializers.newsSerializers import newsListEntity, newsEntity
from src.schemas import CreateNewsSchema, UpdateNewsSchema

router = APIRouter()


@router.get('/')
def get_news(limit: int = 5, page: int = 1):
    skip = (page - 1) * limit
    posts = newsListEntity(News.find().limit(limit).skip(skip))
    return {
        'status': 'success',
        'results': len(posts),
        'posts': posts
    }


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_news(news: CreateNewsSchema):
    news.created_at = datetime.now()
    news.updated_at = news.created_at

    try:
        result = News.insert_one(news.dict())
        new_post = newsEntity(News.find_one(
            filter={
                '_id': result.inserted_id
            }
        ))
        return new_post
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Пост с заголовком '{news.title}' уже существует"
        )


@router.get('/{id}')
def get_news(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Неверный id новости '{id}'"
        )

    news = newsEntity(News.find_one(
        filter={
            '_id': ObjectId(id)
        }
    ))

    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Новость с id '{id} не найдена'"
        )

    return news


@router.put('/{id}')
def update_news(id: str, payload: UpdateNewsSchema):
    if not ObjectId.is_valid(id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Неверный id новости'{id}'"
        )

    updated_news = newsEntity(News.find_one_and_update(
        filter={
            '_id': ObjectId(id)
        },
        update={
            '$set': payload.dict(exclude_none=True)
        },
        return_document=ReturnDocument.AFTER
    ))

    if not updated_news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Новость с id '{id} не найдена'"
        )

    return updated_news


@router.delete('/{id}')
def delete_news(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Неверный id новости'{id}'"
        )

    news = News.find_one_and_delete(
        filter={
            '_id': ObjectId(id)
        }
    )

    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Новость с id '{id} не найдена'"
        )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )
