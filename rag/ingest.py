
import sys
import os
from PyPDF2 import PdfReader
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rag.vector_store import VectorStore


def load_documents(folder="data/manuals"):
    docs = []

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r") as f:
                docs.append(f.read())
        elif file.endswith(".pdf"):
            with open(os.path.join(folder, file), "rb") as f:
                pdf_reader = PdfReader(f)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                docs.append(text)
    print(f"✅ Loaded {len(docs)} documents from {folder}")
    return docs


def ingest():
    docs = load_documents()

    vs = VectorStore()
    vs.create(docs)
    vs.save()

    print(f"✅ Ingested {len(docs)} documents")


if __name__ == "__main__":
    ingest()