# Steve Jobs Chatbot

An AI-powered Streamlit web app that emulates the communication style and mentorship philosophy of **Steve Jobs**.  
The chatbot provides inspirational and practical guidance by retrieving relevant excerpts from Jobs’ real interviews, speeches, and quotes - then crafting context-aware responses using Google’s **Gemini API**.

---

## 🚀 Demo

🌐 [Live App on Streamlit](https://your-app-name.streamlit.app](https://persona-rag-stevejobs-g3zyzeda6xebk4g83zfvmv.streamlit.app/))

---

## 📌 Features

- 💬 **Conversational UI** built with Streamlit  
- 🧠 **FAISS-based retrieval** for contextually relevant answers  
- ⚡ **Sentence Transformers** for semantic embeddings  
- 🤖 **Gemini API integration** for realistic, Jobs-style responses  
- 🗂️ **Curated dataset** from real Steve Jobs interviews, quotes, and speeches  

---

## 🧠 How It Works

1. **Data Collection**  
   - Text scraped and curated from Jobs’ interviews, Stanford speech, and The Lost Interview.  
2. **Embedding & Indexing**  
   - Each text segment is embedded using *Sentence Transformers* (`all-MiniLM-L6-v2`)  
   - Stored in a **FAISS** vector index for fast semantic search.  
3. **Contextual Response Generation**  
   - When a user asks a question, the app retrieves the top relevant text chunks.  
   - A custom prompt blends those insights with Jobs’ speaking style via **Gemini API**.  

---

## 🧰 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **Embedding Model**: Sentence Transformers (`all-MiniLM-L6-v2`)  
- **Vector Store**: FAISS  
- **Language Model**: Google Gemini  
- **Data Sources**: YouTube transcripts, Goodreads quotes, Stanford speech  

---

## 🙋‍♂️ Author

**Ahmed Ragab**  
🎓 Final Year CS Student | AI & Machine Learning Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/ahmed-ragab-29a547218/)
