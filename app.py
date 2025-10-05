import os
import re
import json
import faiss
import numpy as np
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
import streamlit as st


# ================= CONFIG =================
GENAI_API_KEY = "AIzaSyBrhksB5IMcQm_fFsbQZWRRMmVYdw2LPh8"
genai.configure(api_key=GENAI_API_KEY)

DATASET_FILE = "data/steve_jobs_dataset.json"
EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
CHAT_MODEL = "gemini-flash-lite-latest"
TOP_K = 7
# ==========================================



# ============ CLEANING FUNCTION ============
def clean_text(text):
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()
# ==========================================


# ============ BUILD FAISS INDEX ============
@st.cache_resource
def build_faiss_index():
    """Load dataset, embed text, and build FAISS index."""
    with open(DATASET_FILE, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    vectors = [EMBED_MODEL.encode(item["text"]) for item in dataset]
    vectors_np = np.vstack(vectors).astype("float32")

    dim = vectors_np.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors_np)

    return index, dataset, dim
# ==========================================


# ============ CHATBOT FUNCTION ============
def chatbot(query: str, index, dataset):
    query_vector = EMBED_MODEL.encode(query).astype("float32").reshape(1, -1)
    _, I = index.search(query_vector, TOP_K)

    context_chunks = [dataset[i]["text"] for i in I[0]]

    prompt = f"""
You are Steve Jobs, mentoring directly. Speak in a short, practical, conversational style (2–4 sentences max).

Your role is dynamic:

If the user asks for inspiration or motivation, respond with clarity, passion, and vision — like your iconic speeches.

If the user asks a specific question (technical, personal, or business-related), respond with concrete, practical, and actionable advice — not just quotes.

Blend both when appropriate: give real guidance, then tie it back to a bigger vision if it adds value.

Tone: confident, straightforward, and slightly challenging, the way you pushed people to think differently. Avoid being generic. Make the user feel like they’re sitting across from you at a table.

Context for inspiration (use naturally, not forced):
{chr(10).join(context_chunks)}

Question: {query}

Answer like Steve Jobs himself, with passion, clarity, and practical mentorship.
"""

    model = genai.GenerativeModel(CHAT_MODEL)
    response = model.generate_content(prompt)
    return response.text.strip()
# ===========================================


# ====== STREAMLIT UI ======
st.set_page_config(page_title="💬 Steve Jobs Chatbot", page_icon="💡", layout="centered")
st.title("💬 Steve Jobs Chatbot")
st.caption("Ask Steve Jobs for advice, mentorship, or inspiration")

# ---- Reset button ----
if st.button("🔄 Reset Chat"):
    st.session_state["messages"] = []
    st.rerun()

index, dataset, dim = build_faiss_index()


# Chat input
if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.chat_input("Ask Steve Jobs something...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    try:
        answer = clean_text(chatbot(user_input, index, dataset))
        st.session_state["messages"].append({"role": "assistant", "content": answer})
    except Exception as e:
        st.error(f"Error: {e}")

# Display conversation
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])
