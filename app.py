from rag.document_loader import DocumentLoader

loader = DocumentLoader(pdf_dir="documents/pdfs")

documents = loader.load_documents()

print("\n========================")
print(type(documents[0]))
print("\nMetadata : ")
print(documents[0].metadata)
print("\nContents within 500 characters:")
print(documents[0].page_content[:500])