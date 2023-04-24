## Проект «Куда пойти — Москва глазами Артёма»    


Ссылка на сайт: http://alis888.pythonanywhere.com  


### Подготовка к запуску

- Скачайте репозиторий. Установите зависимости:

```sh
git clone https://github.com/Trm888/django_pro_1.git
```
```sh
pip install -r requirements.txt
```

#### Переменные окружения

Создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта. При первом запуске данный ключ находится в файле `settings.py` в переменной `SECRET_KEY`. Перенесите ключ в `.env` и удалите его из `settings.py`.
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `STATIC_URL` — по-умолчанию это `'/static/'`. [Что такое STATIC_URL](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-STATIC_URL).
- `MEDIA_URL` — по-умолчанию это `'/media/'`. [Что такое MEDIA_URL](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-MEDIA_URL).
- `MEDIA_ROOT` — по-умолчанию это `'media'`. [Что такое MEDIA_ROOT](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-MEDIA_ROOT).

### Запуск

- Сделайте миграции:

```sh
python manage.py migrate
```

- Запустите сервер командой

```sh
python manage.py runserver
```
После этого переходите по ссылке http://127.0.0.1:8000/ и сайт будет доступен.

- Создаем суперпользователя:
```sh
python manage.py createsuperuser
```
Теперь можно зайти в админ-панель по адресу: http://127.0.0.1:8000/admin/ и ввести логин и пароль.
Можно добавлять/редактировать локации.

### Заполнение БД

Существует возможность заполнить БД тестовыми данными. Для этого нужно скачать архив с тестовыми данными по ссылке https://github.com/devmanorg/where-to-go-places
Также данные находятся в папке `where-to-go-places-master` в репозитории.
Распаковать архив в папку с проектом.


- Заполнение БД тестовыми данными:
```sh
python manage.py load_place 'путь к папке с файлами'
```
Пример:
```sh
python manage.py load_place 'where-to-go-places-master/places'
```



## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
