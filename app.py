# from rag.document_loader import DocumentLoader
# from rag.document_splitter import SemanticDocumentSplitter
# from rag.text_cleaner import TextCleaner


# loader = DocumentLoader(pdf_dir="documents/pdfs")

# documents = loader.load_documents()

# splitter = SemanticDocumentSplitter(documents)
# chunks = splitter.split_documents(documents)

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

from rag.vectorDB import VectorDatabase
from rag.retrieval_pipeline import Retriever
from rag.llm import UniversityLLM
from deep_translator import GoogleTranslator
from Task2_access.query_manager import QueryManager
from Task2_access.auth import Auth

translator = GoogleTranslator(source_lang="bn", target_lang="en")

def create_context(documents):
    return "\n\n".join(doc.page_content for doc in documents)

def query_language_check(query):
    if any('\u0980' <= ch <= '\u09FF' for ch in query):
        translated_query = translator.translate(query)
        return translated_query
    return query

def source_print(documents):
    print("\n Sources : ")

    checked = set()
    for doc in documents:
        source = doc.metadata.get("title", "Unknown")
        page = doc.metadata.get("page", "?")

        item=(source, page)
        if item not in checked:
            print(f"{source} (Page: {page+1})")
            checked.add(item)
    return "\n".join(f"{source} (Page: {page+1})" for source, page in checked)

def txt_printer(query, ans, src, filename="output.txt"):
    with open(filename, "w", encoding="utf-8") as f:

        f.write("#" * 60 + "\n")
        f.write("DIU AI RESPONSE\n")
        f.write("#" * 60 + "\n\n")

        f.write(f"Question:\n{query}\n\n")
        f.write(f"Answer:\n{ans}\n\n")
        f.write(f"Sources: {source_print(src)}\n\n")


def main():

    print("#"*20)
    print("Welcome to DIU AI")
    print("#"*20)

    auth = Auth()
    session = auth.login()
    if session is None:
        print("\nAuthentication failed")
        return

    vector_db = VectorDatabase()
    vector_db.load_vector_db()

    retriever = Retriever(vector_db)
    llm = UniversityLLM()

    query_manager = QueryManager(retriever=retriever, llm=llm)

    # while True:
    #     query = input("\nAsk what you want to know.......(type 'exit' to quit) ===>>>  \n")

    #     if query.lower() == "exit":
    #         print("\nধন্যবাদ!")
    #         break

    #     docs = retriever.search(query)
    #     context = create_context(docs)
    #     print("=" * 100)
    #     print(context)
    #     print("=" * 100)

    #     # llm hishebe qwen2.5:3b bangla bujhte khub kahini kore tai google translator use kora
    #     en_query = translator.translate(query)
    #     print(f"English Query: {en_query}")
    #     answer = llm.ask(en_query, context)
    #     print(f"Answer: {answer}")
    #     print("\n")
    #     source_print(docs)

    while True:
        query = input("\nAsk what you want to know.......(type 'exit' to quit) ===>>>  \n")

        if query.lower() == "exit":
            print("\nধন্যবাদ!")
            break
        
        query = query_language_check(query)
        result= query_manager.process_query(session=session,query=query)

        txt_printer(query, result["answer"], result["sources"], filename="output.txt")
        print("=" * 100)
        
        print(f"Answer: {result['answer']}")
        source_print(result['sources'])
        print("=" * 100)

if __name__ == "__main__":
    main()