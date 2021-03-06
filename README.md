## О себе
Привет! Меня зовут София, я учусь на программиста и проххожу курсы в Яндекс Практикуме.



## API к учебному проекту Yatube
API доступен аутентифицированным пользователям и доступен по токену TokenAuthentication.Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения. При попытке изменить чужие данные должен возвращаться код ответа 403 Forbidden.
## Для взаимодействия с ресурсами настроены такие эндпоинты:
-   `api/v1/api-token-auth/` (POST): передаём логин и пароль, получаем токен.
-   `api/v1/posts/` (GET, POST): получаем список всех постов или создаём новый пост.
-   `api/v1/posts/{post_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по `id`.
-   `api/v1/groups/` (GET): получаем список всех групп.
-   `api/v1/groups/{group_id}/` (GET): получаем информацию о группе по `id`.
-   `api/v1/posts/{post_id}/comments/` (GET, POST): получаем список всех комментариев поста с `id=post_id` или создаём новый, указав `id` поста, который хотим прокомментировать.
-   `api/v1/posts/{post_id}/comments/{comment_id}/` (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по `id` у поста с `id=post_id`.

## Запуск проекта

1.  Клонирование репозитория

```
git clone https://github.com/PrincessSophie/api_yatube.git

```

Откройте в своем редакторе кода локальный проекта из репозитория GitHub, клонированного ранее

2.  Развертывание в репозитории виртуального окружения

```
python3 -m venv venv

```

3.  Запуск виртуального окружения

```
source venv/Scripts/activate

```

4.  Установка зависимостей в виртуальном окружении

```
pip install -r requirements.txt

```

5.  Выполнение миграций

```
python manage.py migrate

```

6.  Запуск проекта

```
python manage.py runserver

```


