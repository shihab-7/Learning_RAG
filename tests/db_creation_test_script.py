
# testing the db is created or not with the embeddings

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from rag.document_loader import DocumentLoader
from rag.text_cleaner import TextCleaner
from rag.document_splitter import SemanticDocumentSplitter
from rag.vectorDB import VectorDatabase

loader = DocumentLoader(pdf_dir="documents/pdfs")
documents = loader.load_documents()

for doc in documents:
    doc.page_content = TextCleaner.clean(doc.page_content)

splitter = SemanticDocumentSplitter(documents)
chunks = splitter.split_documents(documents)

vector_db = VectorDatabase()
vector_db.create_vector_db(chunks)

print("Database created successfully.")