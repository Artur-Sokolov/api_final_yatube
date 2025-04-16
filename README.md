# API для Yatube

# Установка
Клонируйте репозиторий:
git clone https://github.com/your_username/api_final_yatube.git

Перейдите в директорию проекта:
cd api_final_yatube

Создайте и активируйте виртуальное окружение:
python -m venv venv
source venv/bin/activate

Установите зависимости:
pip install -r requirements.txt

Выполните миграции:
python manage.py migrate

Запустите сервер:
python manage.py runserver

Проект будет доступен по адресу http://127.0.0.1:8000/.

# Примеры запросов
1. Получить список всех постов
Метод: GET
URL: /api/v1/posts/
Аутентификация: Не требуется
curl http://127.0.0.1:8000/api/v1/posts/

2. Создать новый пост
Метод: POST
URL: /api/v1/posts/
Аутентификация: Требуется (JWT-токен)
curl -X POST http://127.0.0.1:8000/api/v1/posts/

3. Получить комментарии к посту
Метод: GET
URL: /api/v1/posts/{post_id}/comments/
Аутентификация: Не требуется
curl http://127.0.0.1:8000/api/v1/posts/1/comments/

4. Добавить комментарий к посту
Метод: POST
URL: /api/v1/posts/{post_id}/comments/
Аутентификация: Требуется (JWT-токен)
curl -X POST http://127.0.0.1:8000/api/v1/posts/1/comments/
