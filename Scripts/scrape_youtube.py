from youtube_transcript_api import YouTubeTranscriptApi
import os

def fetch_transcript(video_id, file_path):
    """Fetches YouTube transcript and saves it as a cleaned text file."""
    transcript = YouTubeTranscriptApi().fetch(video_id)
    clean_text_parts = []
    for snippet in transcript:
        text = snippet.text.strip()
        if text and not (text.startswith('[') and text.endswith(']')):
            clean_text_parts.append(text)

    full_text = ' '.join(clean_text_parts)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(full_text)

def extract_video_id(url):
    """Extracts video ID from YouTube URL."""
    if "youtube.com/watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return url

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    videos = {
        "https://www.youtube.com/watch?v=UF8uR6Z6KLc": "steve_jobs_stanford.txt",
        "https://www.youtube.com/watch?v=vN4U5FqrOdQ": "steve_jobs_iphone_launch.txt",
        "https://www.youtube.com/watch?v=9m68auPIPRk": "steve_jobs_the_lost_interview.txt",
        "https://www.youtube.com/watch?v=YXUhLbV8Nrg": "steve_jobs_MIT.txt"
    }

    for url, filename in videos.items():
        video_id = extract_video_id(url)
        fetch_transcript(video_id, os.path.join("data", filename))

    print("✅ All transcripts fetched and saved in 'data' folder.")