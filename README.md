# 📚 RAG Model using Google Gemini (Python)

This project is a **simple and lightweight Retrieval-Augmented Generation (RAG) system** built using **Google Gemini API** and **Python**.

It allows you to:
- Load documents (PDF / TXT)
- Retrieve relevant context from them
- Ask questions
- Get AI-generated answers grounded only on your documents

This project is **CPU-friendly**, **beginner-friendly**, and runs perfectly in **VS Code**.

---

## 🧠 Architecture (Simple RAG Flow)

Documents → Retrieval → Context → Gemini → Answer

- **Retrieval**: Keyword-based matching (pure Python)
- **Generation**: Google Gemini (Flash-Lite free tier model)

---

## 🛠️ Tech Stack

- Python
- Google Gemini API
- google-genai SDK
- pypdf
- python-dotenv

---

## 📁 Project Structure

RAG-model/
│
├── data/ # PDF / TXT documents
├── rag_gemini.py # Main RAG script
├── requirements.txt
├── .env # Gemini API key (ignored by git)
├── .gitignore
└── README.md


---

## 🔐 Environment Setup

### 1️⃣ Create `.env` file

```env
GEMINI_API_KEY=your_gemini_api_key_here


python -m venv venv

venv\Scripts\activate

source venv/bin/activate

pip install -r requirements.txt


    data/
 ├── notes.txt
 ├── syllabus.pdf

Run the model
python rag_gemini.py

📄 Loaded X document chunks
❓ Ask a question (type 'exit' to quit):

Example
❓ Ask a question: what is this document about

🤖 Answer:
This document explains ...
