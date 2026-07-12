from rag.document_loader import DocumentLoader
from rag.document_splitter import SemanticDocumentSplitter
from rag.text_cleaner import TextCleaner
from rag.vectorDB import VectorDatabase

class IngestionPipeline:

    def __init__(self, pdf_dir):

        self.loader = DocumentLoader(pdf_dir)
        self.cleaner= TextCleaner()
        self.splitter = SemanticDocumentSplitter()
        self.vector_db = VectorDatabase()

    def ingest(self):

        documnets = self.loader.load_documents()

        print(f"Total {len(documnets)} documents loaded.")

        for doc in documnets:
            doc.page_content = self.cleaner.clean(doc.page_content)

        chunks = self.splitter.split_documents(documnets)

        print(f"Total {len(chunks)} chunks created.")

        self.vector_db.create_vector_db(chunks)
        print("Vector database created successfully.")

        return {
            "documents": len(documnets),
            "chunks": len(chunks),
        }