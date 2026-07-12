
# vector db theke top 3 match chunks ber kora
class Retriver:

    def __init__(self, vector_db, search_kwargs={"k": 3}):
        self.vector_db = vector_db
        self.retriever = self.vector_db.get_retriever(search_kwargs={"k": 3})

    def search(self, query):
        if self.retriever is None:
            raise ValueError("Retriever is not initialized. Please create or load the vector database first.")
        return self.retriever.invoke(query)