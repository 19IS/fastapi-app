def newsEntity(news) -> dict:
    return {
        "id": str(news["_id"]),
        "title": news["title"],
        "content": news["content"],
        "image": news["image"],
        "created_at": news["created_at"],
        "updated_at": news["updated_at"]
    }


def newsListEntity(news) -> list:
    return [newsEntity(news_obj) for news_obj in news]
