# Red Mascotera Backend

## Development Setup

### Pre-Requisites

- `Python 3.11`
- `Poetry`
- `Git`

### First Time Setup

1. Clone the repo ...
2. Copy `.env.example` into `.env` and modify as needed
3. CD into the cloned repo and Run `poetry install`
4. Run `poetry shell` to access the virtual environment
5. Run `python manage.py makemigrations` to create the migrations
6. Run `python manage.py migrate` to run migrations
7. Finally `python manage.py runserver` to start the development server


## Project Structure

```
|- red_mascotera <-- Django Project
|- app <--- Django App
|- \ 
|-  | api <--- API Endpoints
|-  | models <--- Database Models
```