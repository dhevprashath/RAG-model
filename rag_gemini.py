import os
from dotenv import load_dotenv
from pypdf import PdfReader
from google import genai

# Load API key
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

DATA_PATH = "data"


def load_documents():
    docs = []
    for file in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, file)

        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                docs.append(f.read())

        elif file.endswith(".pdf"):
            reader = PdfReader(path)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    docs.append(text)

    return docs


def retrieve_context(query, documents, top_k=2):
    query_words = set(query.lower().split())
    scored_docs = []

    for doc in documents:
        doc_words = set(doc.lower().split())
        score = len(query_words & doc_words)
        scored_docs.append((score, doc))

    scored_docs.sort(reverse=True, key=lambda x: x[0])
    top_docs = [doc for score, doc in scored_docs[:top_k]]

    return "\n\n".join(top_docs)[:2000]


def ask_gemini(context, question):
    prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=prompt
    )

    return response.text


def main():
    documents = load_documents()
    print(f"📄 Loaded {len(documents)} document chunks")

    while True:
        query = input("\n❓ Ask a question (type 'exit' to quit): ")
        if query.lower() == "exit":
            break

        context = retrieve_context(query, documents)
        answer = ask_gemini(context, query)

        print("\n🤖 Answer:\n", answer)


if __name__ == "__main__":
    main()
