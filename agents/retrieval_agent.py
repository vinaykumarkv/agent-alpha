from rag.retriever import Retriever

class RetrievalAgent:
    def __init__(self):
        self.retriever = Retriever()

    def fetch_knowledge(self, issue, equipment):
        query = f"{equipment} {issue} troubleshooting"

        docs = self.retriever.get_relevant_docs(query)

        return {
            "query": query,
            "documents": docs
        }