from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


class DocumentLoader:

    def __init__(self, pdf_dir):
        self.pdf_dir = Path(pdf_dir)

    def load_documents(self):
        documents = []

        pdf_files= list(self.pdf_dir.glob("*.pdf"))

        print(f"Total PDF files found: {len(pdf_files)}")

        for pdf in pdf_files:

            print(f"loading PDF ....: {pdf.name}")
            loader = PyPDFLoader(str(pdf))
            docs = loader.load()
            documents.extend(docs)

        print(f"total number of pages from all PDFs : {len(documents)}")
        return documents 