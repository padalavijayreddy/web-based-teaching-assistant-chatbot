# src/test_embedding_storage.py
from document_loader import download_lecture_notes
from document_processor import process_documents
from embeddings import generate_embeddings
from chroma_storage import store_embeddings_in_chroma
from chroma_client import initialize_chroma_client, get_or_create_collection

def test_embedding_storage():
    # Step 1: Download the documents
    documents = download_lecture_notes()

    # Step 2: Extract text from the documents
    extracted_texts = process_documents(documents)

    # Step 3: Generate embeddings for the extracted text
    embeddings = generate_embeddings(extracted_texts)
    
    # Step 4: Store embeddings in ChromaDB
    store_embeddings_in_chroma(extracted_texts, embeddings)

    # Step 5: Check if the collection has documents
    client = initialize_chroma_client()
    collection = get_or_create_collection(client, name="lecture_notes")
    
    if collection.count() > 0:
        print(f"Collection 'lecture_notes' contains {collection.count()} documents.")
    else:
        print("Collection is empty or was not created correctly.")

if __name__ == "__main__":
    test_embedding_storage()
