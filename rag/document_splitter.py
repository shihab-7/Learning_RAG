# chunking the loaded document
# eikhane semantic chunking use kora hoisa karon onno 2 tay context miss korar chance ache

from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

class SemanticDocumentSplitter:

    def __init__(self, documents):
        
        self.embedding_model= HuggingFaceEmbeddings(
            model_name="BAAI/bge-m3"
        )

        self.splitter= SemanticChunker(
            embeddings=self.embedding_model,
            breakpoint_threshold_type="percentile",
            breakpoint_threshold_amount=70
        )
    
    def split_documents(self, documents):

        chunks = self.splitter.split_documents(documents)
        print(f"Total number of chunks after semantic splitting: {len(chunks)}")
        return chunks
