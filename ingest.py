from rag.ingestion_pipiline import IngestionPipeline

pipeline = IngestionPipeline(pdf_dir="documents/pdfs")

summary = pipeline.ingest()
print(f"Ingestion Summary: {summary}")