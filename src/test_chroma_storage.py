# src/test_chroma_storage.py
from document_loader import download_lecture_notes
from document_processor import process_documents
from embeddings import generate_embeddings
from chroma_storage import store_embeddings_in_chroma

def test_store_embeddings():
    documents = download_lecture_notes()  # Download PDFs
    extracted_texts = process_documents(documents)  # Extract text from PDFs
    embeddings = generate_embeddings(extracted_texts)  # Generate embeddings
    
    store_embeddings_in_chroma(extracted_texts, embeddings)  # Store in ChromaDB
    print("Embeddings stored successfully in ChromaDB.")

if __name__ == "__main__":
    test_store_embeddings()
