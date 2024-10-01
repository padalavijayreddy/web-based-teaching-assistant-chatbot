# src/chroma_storage.py
import chromadb
import uuid

def store_embeddings_in_chroma(texts, embeddings):
    """Store embeddings and associated text in Chroma."""
    client = chromadb.Client()
    collection = client.create_collection(name="lecture_notes")  # Create the collection

    for idx, (text, embedding) in enumerate(zip(texts, embeddings)):
        doc_id = str(uuid.uuid4())  # Generate a unique ID for each document
        collection.add(documents=[text], embeddings=[embedding], ids=[doc_id])

    print("Embeddings stored successfully in Chroma.")
