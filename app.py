from rag.document_loader import DocumentLoader
from rag.document_splitter import SemanticDocumentSplitter
from rag.text_cleaner import TextCleaner


loader = DocumentLoader(pdf_dir="documents/pdfs")

documents = loader.load_documents()

splitter = SemanticDocumentSplitter(documents)
chunks = splitter.split_documents(documents)

# Debugging the loaded documents
# print("\n========================")
# print(type(documents[0]))
# print("\nMetadata : ")
# print(documents[0].metadata)
# print("\nContents within 500 characters:")
# print(documents[0].page_content[:500])

# Debugging the chunks
# print("\n========================")
# print(chunks[0].metadata)
# print("\n")
# print(TextCleaner.clean(chunks[0].page_content))



