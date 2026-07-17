from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path

class VectorDatabase:

    def __init__(self, persist_directory="storage/chroma_DB", embedding_model="BAAI/bge-m3"):
        
        base_dir = Path(__file__).resolve().parent.parent
        persist_path = Path(persist_directory)
        if not persist_path.is_absolute():
            persist_path = (base_dir / persist_path).resolve()

        self.persist_directory = str(persist_path)
        self.embedding = HuggingFaceEmbeddings(model_name=embedding_model)
        
        self.db=None

    def create_vector_db(self, chunks):

        self.db=Chroma.from_documents(documents=chunks, embedding=self.embedding, persist_directory=self.persist_directory)
        return self.db
    
    def load_vector_db(self):
        self.db=Chroma(persist_directory=self.persist_directory, embedding_function=self.embedding)
        return self.db
    
    # to see top k match chunks
    def get_retriever(self, search_kwargs={"k": 3}):
        if self.db is None:
            raise ValueError("Vector database is not initialized. Please create or load the database first.")
        return self.db.as_retriever(search_kwargs=search_kwargs)
    
    def get_db(self):
        return self.db