# Mini-CRM: Система бронирования ресурсов

Система для управления студентами, комнатами и бронированиями в учебном центре.

## Установка

1. Клонировать репозиторий
2. Создать виртуальное окружение: `python -m venv venv`
3. Активировать окружение: `venv\Scripts\activate` (Windows) или `source venv/bin/activate` (Unix)
4. Установить зависимости: `pip install -r requirements.txt`
5. Создать базу данных PostgreSQL: `mini_crm`
6. Настроить переменные окружения в файле `.env`
7. Выполнить миграции: `python manage.py migrate`
8. Создать суперпользователя: `python manage.py createsuperuser`
9. Запустить сервер: `python manage.py runserver`

## API Endpoints

- Студенты: `GET/POST /api/students/`
- Загрузка аватара: `POST /api/students/{id}/upload_avatar/`
- Комнаты: `GET/POST /api/rooms/`
- Бронирования: `GET/POST /api/bookings/`

## Документация API

- Swagger: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## Админка

http://localhost:8000/admin/