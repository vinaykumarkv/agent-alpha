from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class VectorStore:
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.db = None

    def create(self, documents):
        self.db = FAISS.from_texts(documents, self.embedding)
        return self.db

    def save(self, path="rag/faiss_index"):
        if self.db:
            self.db.save_local(path)

    def load(self, path="rag/faiss_index"):
        self.db = FAISS.load_local(path, self.embedding)

    def search(self, query, k=3):
        return self.db.similarity_search(query, k=k)
