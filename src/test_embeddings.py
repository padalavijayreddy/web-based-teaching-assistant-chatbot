# src/test_embeddings.py
from document_loader import download_lecture_notes
from document_processor import process_documents
from embeddings import generate_embeddings
from chroma_storage import store_embeddings_in_chroma

def test_embedding_storage():
    # Step 1: Download the documents
    documents = download_lecture_notes()

    # Step 2: Extract text from the documents
    texts = process_documents(documents)

    # Step 3: Generate embeddings for the extracted text
    embeddings = generate_embeddings(texts)

    # Step 4: Store embeddings in ChromaDB
    store_embeddings_in_chroma(texts, embeddings)

if __name__ == "__main__":
    test_embedding_storage()
