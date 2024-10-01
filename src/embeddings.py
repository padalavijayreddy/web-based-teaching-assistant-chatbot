# src/embeddings.py
import openai
from config import OPENAI_API_KEY

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

def generate_embeddings(texts):
    """Generate embeddings for a list of texts using OpenAI's latest API."""
    embeddings = []
    for text in texts:
        response = openai.embeddings.create(input=text, model="text-embedding-ada-002")
        embedding = response.data[0].embedding  # Correctly access the embedding from the response
        embeddings.append(embedding)
    return embeddings
