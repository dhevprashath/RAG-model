# Simple RAG Project (CPU Only)

## Setup

### 1. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

### 2. Install dependencies
pip install -r requirements.txt

### 3. Add documents
Put .txt or .pdf files into the data/ folder

### 4. Build vector database
python ingest.py

### 5. Ask questions
python rag_query.py
