# Тестовое задание DocuSketch.
### 1. Bash скрипт для контроля памяти ram с отправкой alarm на внешний API.
 - Скрипт каждые 5 минут проверяет заполненность памяти.
 - При использовании 90% памяти отправляет alarm на внешний сервер.
 - Запрос на внешний сервер отправляется при помощи утилиты curl.
##### Установка и запуск на Ubuntu 20.04 server:

```
    1. Склонировать репозиторий на сервер и перейти в папку "ramcheck_bash"
    2. Изменить в файле script.sh переменные API_ENDPOINT и APIKEY для доступа авторизации на сервере
    3. Ввести команду для установки "sh install.sh"
```

### 2. Приложение на Flask
 - Приложение принимает GET, POST, PUT запросы в endpoint /key
 - Приложение слушает порт 8080
 - В качестве базы данных используется MongoDB
 - Приложение и база данных разворачиваются при помощи docker-compose
 - Файлы базы данных сохраняются при помощи volumes в папке data
##### Установка и запуск на Ubuntu 20.04 server:

```
    1. Склонировать репозиторий на сервер и перейти в папку "flask_app"
    2. Установить на сервер Make и docker-compose при помощи команды "sh install.sh"
    3. Запустить сервер при помощи команды make run
```
## Документация по API:
#### 1. Поиск ключа в базе.
###### GET запрос - /key 
 - Принимает парамаетр key в query.
 - Возвращает:
    1. Если ключ имеется в базе: ```{"status": 0, "message": "Key found", "key": KEY, "value": KEY_VALUE```
    2. Если ключа в базе нет: ```{"status": 4, "message": "Key not found", "key": None, "value": None}```

#### 2. Добавление ключа в базу.
###### POST запрос - /key
 - Принимает JSON вида ```{"key": KEY, "value": VALUE}```
 - Возвращает:
    1. Если ключ добавлен в базу ```{"status": 0, "message": "Key added", "key": KEY, "value": VALUE}```
    2. Если ключ уже есть в базе ```{"status": 1, "message": "The key already exists", "key": KEY, "value": None}```

#### 3. Изменение ключа в базе.
###### PUT запрос - /key
 - Принимает JSON вида ```{"key": KEY, "value": VALUE}```
 - Возвращает:
    1. Если ключ изменен ```{"status": 0, "message": "Key updated", "key": KEY, "value": VALUE}```
    2. Если ключ ключ в базе уже имеет такое значение ```{"status": 7, "message": "The key has already been updated", "key": KEY, "value": VALUE}```
    3. Если ключ в базе не найден ```{"status": 6, "message": "Value not found", "key": None, "value": None}```