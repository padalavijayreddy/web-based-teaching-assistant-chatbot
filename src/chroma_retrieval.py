# src/chroma_retrieval.py
import openai
from config import OPENAI_API_KEY
import chromadb

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

def retrieve_relevant_content(query, collection, k=3):
    """Retrieve the top-k most relevant documents based on the user's query."""
    # Generate query embedding using OpenAI API
    response = openai.embeddings.create(input=query, model="text-embedding-ada-002")
    query_embedding = response.data[0].embedding  # Access the embedding correctly

    # Perform similarity search in Chroma collection
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results['documents']  # Return the top-k most relevant documents
