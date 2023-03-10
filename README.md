# fastapi-app

**fastapi-app** - REST API, разрабатываемое в ходе курса "Веб программирование".

## Локальная установка и запуск

> :warning: Для локального запуска приложения необходимо установить [docker и docker-compose](https://docs.docker.com/desktop/install/mac-install/).

> :warning: Все команды приведены для Linux (Ubuntu).

1. Создайте docker-контейнеры с помощью команды:

```bash
docker-compose -f docker-compose.yml build
```

2. Запустите docker-контейнеры с помощью команды:

```bash
docker-compose -f docker-compose.yml up
```

3. Для доступа к клиентской части приложения перейдите по ссылке http://127.0.0.1:8000

## Работа с API

> :warning: Не забудте сначала запустить docker-контейнеры

Для работы с API перейдине на страницу [Интерактивная документация](http://127.0.0.1:8000/docs)
  
Для запуска тестов откройте контейнер `fastapi_container` и введите команду:

```bash
python -m pytest .
```
