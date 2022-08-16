# police_appeals

Для работы нужно:

1. Создать виртуальное окружение
`python3 -m venv venv`

2. Установить зависимости через команду
`pip install -r requirements`

3. Создать файл `settings_local.py` И добавить секреты для доступа к базе (DATABASES), и так же пусть к csv файлу (CVS_FILE_PATH)

4. Сделать миграции для базы данных 
`python manage.py migrate`

5. Запустить команду для загрузки данных в бд из csv файла
`python manage.py load_reports`

6. Запустить сервер, для доступа к API
`python manage.py runserver`


API:

GET /api/reports
query:
limt: int
page: int
date_from: int (timestamp)
date_to : int (timestamp)


PS: Так же можно поменять INSERT_BY_STEP переменную в settings_local.py чтобы изменить колличество строк для записи за 1 транзакцию
