# src/test_vectorstore.py
from vectorstore import embed_and_store_documents

def test_vectorstore():
    vectorstore = embed_and_store_documents()
    print("Documents embedded and stored in vector store successfully.")

if __name__ == "__main__":
    test_vectorstore()
