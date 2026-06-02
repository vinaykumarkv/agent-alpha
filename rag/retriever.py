from rag.vector_store import VectorStore


class Retriever:
    def __init__(self):
        self.vs = VectorStore()
        self.vs.load()

    def get_relevant_docs(self, query):
        results = self.vs.search(query)

        return [doc.page_content for doc in results]