import os
import json

def load_quotes(quotes_file):
    with open(quotes_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    dataset = [{"text": q.strip(), "source": "GoodReads", "type": "quote"} for q in data if q.strip()]
    return dataset
