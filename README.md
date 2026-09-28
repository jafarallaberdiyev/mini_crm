# Mini-CRM — Room Booking System

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.14-A30000)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

REST API for a training center: manage **students**, **rooms** and **bookings**, with protection against double-booking a room for overlapping time slots.

> 🇷🇺 Система для управления студентами, комнатами и бронированиями в учебном центре. Инструкция по установке ниже.

## Features

- **Students** — CRUD, unique email, avatar upload to Cloudinary
- **Rooms** — lecture / computer / conference / studio types with capacity
- **Bookings** — time-slot reservations with overlap (conflict) checks
- Pagination, Swagger & ReDoc API docs, Django admin

## Tech stack

Django 4.2 · Django REST Framework · PostgreSQL · Cloudinary · drf-yasg

## Getting started / Установка

```bash
git clone https://github.com/jafarallaberdiyev/mini_crm.git
cd mini_crm/mini_crm

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
cp .env.example .env           # then fill in your own values
```

Create a PostgreSQL database named `mini_crm` (or set `DB_NAME` in `.env`), then:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## API endpoints

| Resource | Endpoint |
|---|---|
| Students | `GET/POST /api/students/` |
| Upload avatar | `POST /api/students/{id}/upload_avatar/` |
| Rooms | `GET/POST /api/rooms/` |
| Bookings | `GET/POST /api/bookings/` |

## API docs

- Swagger UI — http://localhost:8000/swagger/
- ReDoc — http://localhost:8000/redoc/
- Admin — http://localhost:8000/admin/

## License

[MIT](LICENSE)
