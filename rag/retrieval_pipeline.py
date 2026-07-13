# vector db theke top 3 match chunks ber kora
class Retriever:

    def __init__(self, vector_db):
        self.db = vector_db.get_db()

    def search(self, query,k=5, threshold=0.36):
        
        results = self.db.similarity_search_with_relevance_scores(query=query, k=k)

        documents = []
        for doc, score in results:
            print(f"Score: {score:.3f} --> {doc.metadata['title']}")
            if score >= threshold:
                documents.append(doc)
    
        return documents
