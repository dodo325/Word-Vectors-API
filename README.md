# Word-Vectors-API
FastAPI for gensim nlp models

# Запуск
## Подготовка моделей:
1. Качаем модель
```bash
    wget http://vectors.nlpl.eu/repository/20/187.zip -P models
```

2. Распоковываем:
```bash
    unzip 214.zip -d geowac_tokens_none_fasttextskipgram_300_5_2020
```

## Локальный запуск:
1. Устанавливаем зависимости:
```bash
    pip install -r requirements.txt
```

2. Запускаем через 

```
    uvicorn main:app --reload
```

## Запуск через Docker
Сборка:
```bash
    docker build -t wv-api .
```

В тестовом режиме:
```bash
    docker run -it -v "$(pwd)"/models/:/app/models/ -p 8080:80 wv-api
```

или в фоновом режиме:

```bash
    docker run -d -v "$(pwd)"/models/:/app/models/ -p 80:80 wv-api
```
