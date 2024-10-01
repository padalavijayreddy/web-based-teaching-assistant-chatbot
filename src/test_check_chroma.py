# src/test_check_chroma.py
from chroma_client import initialize_chroma_client, get_or_create_collection
import chromadb  # Ensure this is imported

def check_chroma_collection():
    client = initialize_chroma_client()
    try:
        collection = get_or_create_collection(client, name="lecture_notes")
        print(f"Collection 'lecture_notes' contains {collection.count()} documents.")
        
        # Retrieve only documents (you can add more if needed)
        documents = collection.get(include=['documents'])
        for idx, doc in enumerate(documents['documents']):
            print(f"Document {idx + 1}: {doc}")
    except chromadb.errors.InvalidCollectionException:
        print("Collection 'lecture_notes' does not exist.")

if __name__ == "__main__":
    check_chroma_collection()
