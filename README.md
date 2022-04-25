# Установка

## Предварительно нужно создать и активировать виртуальное окружение, а также запустить сервер mongodb. Затем в директории с проектом:
```sh
pip install -r requirements.txt
```
## Затем необходимо создать .env c переменными: VK_API_ACCESS_TOKEN, VK_API_VERSION, MONGO_HOST_NAME, MONGO_PORT, MONGO_DATABASE_NAME. В конце запуск проекта:
```sh
python manage.py runserver
```
