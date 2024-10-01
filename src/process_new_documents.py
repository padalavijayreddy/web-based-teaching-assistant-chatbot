# src/process_new_documents.py
from document_loader import download_lecture_notes
from document_processor import process_documents
from embeddings import generate_embeddings
from chroma_storage import store_embeddings_in_chroma

def process_and_store_new_documents():
    # Step 1: Download all the lecture notes (including newly added PDFs)
    documents = download_lecture_notes()  # This now includes your extended list of URLs

    # Step 2: Extract text from each document
    texts = process_documents(documents)

    # Step 3: Generate embeddings for the extracted text
    embeddings = generate_embeddings(texts)

    # Step 4: Store embeddings in ChromaDB
    store_embeddings_in_chroma(texts, embeddings)

if __name__ == "__main__":
    process_and_store_new_documents()
