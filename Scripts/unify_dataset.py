import os
import json

def load_quotes(quotes_file):
    with open(quotes_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    dataset = [{"text": q.strip(), "source": "GoodReads", "type": "quote"} for q in data if q.strip()]
    return dataset

def load_transcripts(transcript_folder, chunk_size=50):
    dataset = []
    for file in os.listdir(transcript_folder):
        if file.endswith(".txt"):
            path = os.path.join(transcript_folder, file)
            with open(path, "r", encoding="utf-8") as f:
                words = f.read().split()
            for i in range(0, len(words), chunk_size):
                chunk = " ".join(words[i:i+chunk_size]).strip()
                if chunk:
                    dataset.append({"text": chunk, "source": file, "type": "speech"})
    return dataset

if __name__ == "__main__":
    dataset = []

    quotes_file = "data/steve_jobs_quotes.json"
    transcript_folder = "data"
    output_file = "data/steve_jobs_dataset.json"

    if os.path.exists(quotes_file):
        dataset.extend(load_quotes(quotes_file))
    if os.path.exists(transcript_folder):
        dataset.extend(load_transcripts(transcript_folder))

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
