# Flask Easy Blank

Шаблон проекта на Flask с REST API (Flask-RESTX) и SQLAlchemy.

**Кратко:** приложение предоставляет простые CRUD-эндпоинты для фильмов, режиссеров и жанров и использует SQLite (по умолчанию — in-memory) для хранения данных.

**Структура**
- `main.py` — точка входа приложения, создание и регистрация расширений
- `setup_db.py` — инициализация `SQLAlchemy` (объект `db`)
- `config.py` — конфигурация приложения (URI БД и др.)
- `dao/` — модели и схемы marshmallow
- `views/` — REST-эндоинты (movies, directors, genres)
- `services/`, `container.py` — бизнес-логика и DI-контейнер (зависимости)

**Требования**
Установите зависимости из `requirements.txt` (в папке `app`):

```powershell
python -m pip install -r app/requirements.txt
```

Если используете виртуальное окружение — активируйте его перед установкой.

**Запуск**
По умолчанию приложение использует SQLite в памяти (`sqlite:///:memory:`). Для запуска:

```powershell
& C:\Users\Администратор\AppData\Local\Programs\Python\Python314\python.exe "c:/Users/Администратор/Desktop/homework 18/app/main.py"
```

После запуска API будет доступно на `http://127.0.0.1:5000/`.

Чтобы сохранить БД в файл, откройте `app/config.py` и замените `SQLALCHEMY_DATABASE_URI` на, например:
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
```

и перезапустите приложение.

**Основные эндпоинты**
- `GET /movies/` — список фильмов (поддерживает фильтрацию: `?director_id=..&genre_id=..&year=..`)
- `POST /movies/` — создать фильм
- `GET /movies/<id>` — получить фильм по id
- `PUT /movies/<id>` — обновить фильм
- `DELETE /movies/<id>` — удалить фильм

- `GET /directors/` — список режиссеров
- `GET /directors/<id>` — режиссер по id

- `GET /genres/` — список жанров
- `GET /genres/<id>` — жанр по id

(Все эндпоинты регистрируются через Flask-RESTX и доступны в документации Swagger, если вы подключите UI.)

**Замечания по отладке**
- В коде используется `db.create_all()` внутри инициализации, чтобы создать таблицы (особенно важно при использовании in-memory SQLite).
- Если вы видите, что при `GET /movies` возвращаются режиссеры — проверьте `app/views/directors.py`: namespace должен быть `Namespace('directors')`, а не `movies`.
- Если возникают ошибки с внешними ключами — убедитесь, что в моделях `ForeignKey` ссылаются на правильные имена таблиц (`genres`, `directors`).

