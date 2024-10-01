# src/chroma_storage.py
from chroma_client import initialize_chroma_client, get_or_create_collection
import uuid

def store_embeddings_in_chroma(texts, embeddings):
    """Store embeddings and associated text in ChromaDB."""
    client = initialize_chroma_client()  # Initialize ChromaDB client
    collection = get_or_create_collection(client, name="lecture_notes")  # Create or get the collection

    # Logging to check the size of embeddings and texts
    print(f"Storing {len(texts)} texts and {len(embeddings)} embeddings in the collection.")

    for idx, (text, embedding) in enumerate(zip(texts, embeddings)):
        doc_id = str(uuid.uuid4())  # Generate unique ID for each document
        
        # Add a print statement to confirm each document is being added
        print(f"Storing document {idx + 1} with ID: {doc_id}")
        print(f"Document text (first 100 chars): {text[:100]}")
        print(f"Embedding (first 10 values): {embedding[:10]}")
        
        collection.add(documents=[text], embeddings=[embedding], ids=[doc_id])

    print("Embeddings stored successfully in ChromaDB.")
