# Проект "Трекер полезных привычек"  
  
## Описание проекта  
  
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.  
В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше двух минут.  
Чем отличается полезная привычка от приятной и связанной?
Полезная привычка — это само действие, которое пользователь будет совершать и получать за его выполнение определенное вознаграждение (приятная привычка или любое другое вознаграждение).

Приятная привычка — это способ вознаградить себя за выполнение полезной привычки. Приятная привычка указывается в качестве связанной для полезной привычки (в поле «Связанная привычка»).

Например: в качестве полезной привычки вы будете выходить на прогулку вокруг квартала сразу же после ужина. Вашим вознаграждением за это будет приятная привычка — принять ванну с пеной. То есть такая полезная привычка будет иметь связанную привычку.

Рассмотрим другой пример: полезная привычка — «я буду не опаздывать на еженедельную встречу с друзьями в ресторан». В качестве вознаграждения вы заказываете себе десерт. В таком случае полезная привычка имеет вознаграждение, но не приятную привычку.  
  
  
## Возможности проекта  

- Регистрация и авторизация пользователей
- Создание, просмотр, обновление и удаление привычек
- Просмотр списка привычек пользователей
- Просмотр общедоступных привычек
- Интеграция с мессендером Telegram


## Используемое окружение

- Python
- virtual environment
- Django (DRF, Celery)
- PostgreSQL
- Telegram API


## Запуск и использование

1) Склонировать проект из репозитория:
    https://github.com/Art9Mor/cw_8_habits.git  
2) Установить Docker
    www.docker.com
3) Установить зависимости из текстового документа  requirements.txt
    - pip install -r requirements.txt
4) Создать и заполнить своими данными файл .env, поля для заполнения взять из файла .env.example
    - DATABASE_NAME=<имя_базы_данных>
    - DATABASE_USER=<имя_пользователя>
    - DATABASE_PASSWORD=<пароль_базы_данных>
    - DATABASE_HOST=<хост_базы_данных(db)>
    
    - EMAIL_HOST_USER=<почта_для_рассылки>
    
    - CORS_ALLOWED_ORIGINS=<>
    
    - CELERY_TIMEZONE=<ваше_местное_время(Europe/Moscow)>
    - CELERY_BROKER_URL=<url_адрес_брокера_celery(redis://redis:6379)>
    - CELERY_RESULT_BACKEND=<url_бэкенда>
    
    - TELEGRAM_URL=<url_адрес_Telegram>
    - TELEGRAM_TOKEN=<токен_Telegram_бота(https://api.telegram.org/bot)>
5) Применить миграции
    - python manage.py migrate
6) Запустить сервер
    - python manage.py runserver
7) Запустить Celery для обработки отложных задач
    - celery -A config worker --pool=solo -l INFO
    - celery -A config beat -l info -S django
8) При необходимости создать суперпользователя
    - python manage.py csu
   Параметры суперпользователя: email = 'habit@hell.aid', password = 666
9) При необходимости заполнить базу данных тестовыми данными
    - python manage.py fill_habits
    - python manage.py fill_users
10) Создать токен для работы с Telegram
   - перейти по ссылке https://t.me/BotFather
   - начать диалог командой /start
   - создать нового бота командой /newbot
   - ввести имя бота (оно будет отображаться пользователям)
   - ввести юзернэйм бота (уникальный идентификатор который должен заканчиваться на _bot)
   - скопировать токен в соответствующее поле файла .env


## API проекта
Доступ к документации будет осуществляться после запуска проекта по адресу http://localhost:8000/redoc/


## Docker
Для создания и работы с Docker необходимо выполнить следующие шаги:
   1) Установить приложение Docker в зависимости от Вашей ОС по инструкции: https://docs.docker.com/engine/install/
   2) Запустить Docker
   3) Ввести в консоли виртуального окружения проекта следующие команды:
      - docker compose build
      - docker compose up
        (В случае ошибки с сообщением "`coreapi` must be installed for schema support" следует ввести команду:  
            - pip install coreapi pyyaml  
         После чего повторить команды пункта 3).

