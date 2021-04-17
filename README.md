# Word-Vectors-API
FastAPI for gensim nlp models


## Запуск:
0. Устанавливаем зависимости:
```bash
    pip install -r requirements.txt
```

1. Качаем модель
```bash
    wget http://vectors.nlpl.eu/repository/20/187.zip -P models
```

2. Распоковываем:
```bash
    unzip 214.zip -d geowac_tokens_none_fasttextskipgram_300_5_2020
```

3. Запуск через 

```
    uvicorn main:app --reload
```

