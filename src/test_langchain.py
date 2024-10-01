# src/test_langchain.py
from langchain_integration import ingest_documents_to_chroma, query_documents

def test_langchain_workflow():
    # Step 1: Ingest the lecture notes into Chroma using LangChain
    pdf_paths = [
        "data/cs188-su24-lec01.pdf",
        "data/cs188-su24-lec02.pdf",
        "data/cs188-su24-lec03.pdf",
        "data/cs188-su24-lec04.pdf",
        "data/cs188-su24-lec05.pdf"
    ]
    ingest_documents_to_chroma(pdf_paths)

    # Step 2: Query the documents
    query = "What is Artificial Intelligence?"
    answer = query_documents(query)
    print(f"Answer: {answer}")

if __name__ == "__main__":
    test_langchain_workflow()
