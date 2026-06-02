
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rag.vector_store import VectorStore


def load_documents(folder="data/manuals"):
    docs = []

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r") as f:
                docs.append(f.read())

    return docs


def ingest():
    docs = load_documents()

    vs = VectorStore()
    vs.create(docs)
    vs.save()

    print(f"✅ Ingested {len(docs)} documents")


if __name__ == "__main__":
    ingest()