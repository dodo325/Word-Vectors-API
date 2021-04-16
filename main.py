from gensim.models import KeyedVectors
from fastapi import FastAPI

app = FastAPI()
m_file = "models/geowac_tokens_none_fasttextskipgram_300_5_2020/model.model"

items = {}
@app.on_event("startup")
async def startup_event():
    items["model"] = KeyedVectors.load(m_file, mmap='r')

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/similarity/{word_1}/{word_2}")
async def get_similarity(word_1: str, word_2: str):
    val = float(items["model"].similarity(word_1, word_2))
    return {"value": val}
