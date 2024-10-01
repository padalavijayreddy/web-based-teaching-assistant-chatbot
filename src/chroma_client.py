# src/chroma_client.py
import chromadb

def initialize_chroma_client():
    """Initializes and returns the ChromaDB client with persistence."""
    client = chromadb.Client()  # No need to specify persistence here
    return client

def get_or_create_collection(client, name="lecture_notes"):
    """Gets or creates the ChromaDB collection."""
    try:
        return client.get_collection(name=name)
    except chromadb.errors.InvalidCollectionException:
        return client.create_collection(name=name)
