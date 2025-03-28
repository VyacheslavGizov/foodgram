[![Main Foodgram workflow](https://github.com/VyacheslavGizov/foodgram/actions/workflows/main.yml/badge.svg)](https://github.com/VyacheslavGizov/foodgram/actions/workflows/main.yml)

## Описание проекта:

Проект «Фудграм» (foodgram-project.hopto.org) — сайт, на котором пользователи могут публиковать свои рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Зарегистрированным пользователям также доступен сервис «Список покупок». Он позволит создавать список продуктов, которые нужно купить для приготовления выбранных блюд.
Проект состоит из следующих страниц: 
- главная: содержит первые шесть рецептов, отсортированные по дате, остальные рецепты доступны на следующих страницах;
- страница входа,
- страница регистрации,
- страница рецепта: содержит полное описание рецепта, залогиненные пользователи могут добавить рецепт в избранное список покупок, подписаться на автора рецепта.
- страница пользователя: содержит имя пользователя, все рецепты опубликованные пользователем и кнопку для  подписки/отписки от него;
- страница подписок: доступна только владельцу аккаунта и содержит перечисление авторов, на которых подписан пользователь.
- избранное: добавлять рецепты в избранное может только залогиненный пользователь.
- список покупок: доступен только залогинненым пользователям.
- создание и редактирование рецепта: доступна только залогинненым пользователям, все поля обязательны для заполнения
- страница смены пароля.

Добавить новые теги и ингредиенты может только администратор через админку: foodgram-project.hopto.org/admin

## Ссылки:
- [Проект «Фудграм»](https://foodgram-project.hopto.org/)
- [Документация к API «Фудграм»](https://foodgram-project.hopto.org/api/docs/)

## Стек:
- Django REST
- Docker
- Gunicorn
- JS
- Nginx
- Node.js
- PostgreSQL
- Python 3.9

## Как запустить проект:
### Для того, чтобы развернуть проект с использованием Docker, необходимо:
1. Установить Docker:
- для [Windows и MacOS](https://www.docker.com/products/docker-desktop/);
- для [Linux](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script);
- Если вы работаете на Linux, то также необходимо отдельно установить [Docker Compose](https://docs.docker.com/compose/install/).
2. Клонировать репозиторий:
```
git clone https://...
```
3. В директории проекта foodgram создать файл .env с переменными окружения:
```
# Содержимое .env
POSTGRES_DB=<имя_базы_данных>
POSTGRES_USER=<имя_пользователя_базы_данных>
POSTGRES_PASSWORD=<пароль_пользователя_базы_данных>

DB_HOST=db  # Адрес, по которому Django будет соединяться с БД. В данном случае имя контейнера с БД.
DB_PORT=5432  # Порт, по которому Django будет обращаться к БД.

USE_SQLITE=False  # Если True, то будет использована БД sqlite.

SECRET_KEY=<секретный_ключ_Django>
DEBUG=False  # Для отладки True.
ALLOWED_HOSTS=<IP_и/или_доменное имя>
```
4. Для запуска контейнеров, находясь в корневой директории проекта, выполнить:
```
docker compose up  # Запуск контейнеров.
docker compose exec backend python manage.py migrate  # Миграции.
docker compose exec backend python manage.py load_ingredients_from_json  # Загрузить продукты.
docker compose exec backend python manage.py load_tags_from_json  # Загрузить теги.
docker compose exec backend python manage.py collectstatic  # Сбор статики.
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/  # Перемещение статики.
```

### Для того, чтобы развернуть проект локально без Docker, необходимо:
1. Установить Node.js версии v21.7.3 c [официального сайта](https://nodejs.org/en/about/previous-releases#looking-for-latest-release-of-a-version-branch).
2. Выполнить шаги 2 и 3 из инструкции с применением Docker.
3. Перейти в директорию foodgram/backend/, создать и активировать виртуальное окружение, установить зависимости:
```
cd backend/
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
5. Дополнительно установить django-cors-header:
```
pip install django-cors-headers 
```
6. Открыть backend/config/settings.py:
- подключить django-cors-header как приложение:

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',  # Добавить
    ...
]
```
- в списке MIDDLEWARE зарегистрировать CorsMiddleware выше CommonMiddleware:
```
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',  # Добавить
    'django.middleware.common.CommonMiddleware',
    ...
]
```
- добавить константы:
```
CORS_URLS_REGEX = r'^/api/.*$' 
CORS_ALLOWED_ORIGINS = ['http://localhost:3000',] 
```
8. Вернуться в директорию backend/ и выполнить:
```
python manage.py migrate  # Миграции.
python manage.py load_ingredients_from_json  # Загрузить продукты.
backend python manage.py load_tags_from_json  # Загрузить теги.
python manage.py runserver  # Запустить отладочный веб-сервер.
```
7. В новом окне терминала перейти в директорию foodgram/frontend/, установить зависимости и запустить приложение на React:
```
npm i 
npm run start 
```
## Авторы:
- [ЯП](https://github.com/yandex-praktikum);
- [Vyacheslav Gizov](https://github.com/VyacheslavGizov).