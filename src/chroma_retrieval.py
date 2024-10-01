# src/chroma_retrieval.py
from chroma_client import initialize_chroma_client, get_or_create_collection
import openai

def retrieve_relevant_content(query, k=3):
    """Retrieve the top-k most relevant documents based on the user's query."""
    client = initialize_chroma_client()  # Initialize ChromaDB client
    collection = get_or_create_collection(client, name="lecture_notes")  # Get the ChromaDB collection

    # Generate query embedding using OpenAI API
    response = openai.Embedding.create(input=query, model="text-embedding-ada-002")
    query_embedding = response['data'][0]['embedding']  # Access the embedding correctly

    # Perform similarity search in Chroma collection
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results['documents']  # Return the top-k most relevant documents
