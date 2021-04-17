from gensim.models import KeyedVectors
from fastapi import FastAPI
from pathlib import Path
from typing import Optional


app = FastAPI()
items = {}


def get_models_dirs(base_dir = "models"):
    path = Path(base_dir)
    return [x for x in path.iterdir() if x.is_dir()]


def get_model_by_name(model_name: str) -> Optional[KeyedVectors]:
    models_dirs = get_models_dirs()
    for model_dir in models_dirs:
        if model_dir.name == model_name:
            model_file = model_dir / "model.model"
            return KeyedVectors.load(str(model_file), mmap='r')


@app.on_event("startup")
async def startup_event():
    models_dirs = get_models_dirs()
    model_file = models_dirs[0] / "model.model"
    items["model"] = KeyedVectors.load(str(model_file), mmap='r')
    items["model_name"] = models_dirs[0].name


@app.get("/models/")
async def read_root():
    return [
            str(x.name) for x in get_models_dirs()
        ]


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/similarity/{word_1}/{word_2}")
async def get_similarity(word_1: str, word_2: str):
    val = float(items["model"].similarity(word_1, word_2))
    return {
        "value": val,
        "word_1": word_1,
        "word_2": word_2,
        "model_name": items["model_name"]
        }
