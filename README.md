# Steve Jobs Persona Chatbot

A Retrieval-Augmented Generation (RAG) chatbot inspired by Steve Jobs' public interviews, speeches, and quotes.

The application retrieves relevant text from a curated dataset and uses Google's Gemini API to generate conversational responses.

## Live Demo

[Try the application](https://persona-rag-stevejobs-g3zyzeda6xebk4g83zfvmv.streamlit.app/)

## Features

- Conversational interface built with Streamlit.
- Semantic search using Sentence Transformers.
- FAISS-based vector retrieval.
- Gemini-powered response generation.
- Curated dataset containing 713 text segments.

## How It Works

1. Load the curated Steve Jobs dataset.
2. Generate text embeddings using `all-MiniLM-L6-v2`.
3. Store embeddings in a FAISS index.
4. Retrieve the 7 most relevant text segments for each question.
5. Pass the retrieved context to Gemini to generate a response.

## Dataset

The dataset contains excerpts from:

- Steve Jobs' Stanford commencement speech.
- The Lost Interview.
- MIT interview.
- iPhone launch presentation.
- Goodreads quotes.

## Tech Stack

- Python
- Streamlit
- Sentence Transformers
- FAISS
- Google Gemini API
- NumPy

## Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/ahmed17717/Persona-RAG-SteveJobs.git
   cd Persona-RAG-SteveJobs
   
2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3.Create a .env file and add your Gemini API key:

   ```bash
   GEMINI_API_KEY=your_api_key_here
   ```
4. Run the application:

   ```bash
   streamlit run app.py
