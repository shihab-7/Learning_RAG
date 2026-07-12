import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from rag.vectorDB import VectorDatabase
from rag.retrieval_pipeline import Retriver

vector_db = VectorDatabase()
vector_db.load_vector_db()
retriever = Retriver(vector_db)

search_query = "Admission opening date?"

docs = retriever.search(search_query)

for i, doc in enumerate(docs):
    print(f"\n======================== Document {i+1} ========================")
    print(doc.metadata)
    print("\n")
    print(doc.page_content)