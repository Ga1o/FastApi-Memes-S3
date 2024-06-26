# Meme API

API для работы с коллекцией мемов, используя FastAPI.

## Функциональность
- Получить список всех мемов с пагинацией
- Получить мем по id
- Добавить мем 
- Обновить мем
- Удалить мем

## Установка и запуск

### Требования
- Docker
- Docker Compose
- Git

### Запуск
1. Клонируйте репозиторий:
   ```
   git clone https://github.com/Ga1o/FastApi-Memes-S3.git
   cd fastapi-memes-s3
   ```
2. Утановите зависимости:
   ```
   pip install -r riquirements.txt
   ```
3. Создайте файл `.env` и добавьте переменные окружения.
4. Запустите контейнер:
   ```
   docker-compose up --build
   ```   
5. API:
   ```
   http://localhost:8000/
   http://localhost:8000/memes
   http://localhost:8000/docs
   ```  

## Тестирование
Чтобы запустить тесты, используйте следующую команду:
   ```
   pytest
   ```  