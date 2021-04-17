""" Это базовый клиент для Python

Для его работы необходимо установить библиотеку requests:

    pip install requests
"""
import requests

def words_similarity(
    w1: str, w2: str, 
    base_url="127.0.0.1:80"
    model="geowac_lemmas_none_fasttextskipgram_300_5_2020", timeout=1
) -> float:
    """Вычисление коэффициента близости между двумя словами с помошью API
    Args:
        w1 (str): Первое слово
        w2 (str): Второе слово
        model (str, optional): Модель NLP. Defaults to 'geowac_lemmas_none_fasttextskipgram_300_5_2020'.

    Returns:
        float: Коэффицент симммантической близости
    """
    url = "/".join(
        [base_url, "similarity", w1 , w2]
    )
    r = requests.get(url, stream=True, timeout=timeout)
    val = r.json()["value"]
    return val
