import openai
from chroma_retrieval import retrieve_relevant_content
from config import OPENAI_API_KEY
import chromadb

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def get_answer(query):
    """Main function to retrieve content and generate an answer based on the query."""
    client = chromadb.Client()

    # Check if collection exists, if not, create it
    try:
        collection = client.get_collection(name="lecture_notes")  # Get the ChromaDB collection
    except chromadb.errors.InvalidCollectionException:
        print("Collection 'lecture_notes' does not exist. Creating it now...")
        collection = client.create_collection(name="lecture_notes")

    # Step 1: Retrieve relevant documents from ChromaDB
    relevant_documents = retrieve_relevant_content(query, collection)
    
    # If documents are empty, return a fallback response
    if not relevant_documents or relevant_documents == [[]]:
        return "No relevant documents found for the query."

    # Flatten the relevant documents if necessary
    context = " ".join([doc for doc in relevant_documents if isinstance(doc, str)])

    # Step 2: Use OpenAI's GPT model to generate an answer based on the retrieved documents
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4 if you're using GPT-4
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on AI lecture notes."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ],
        max_tokens=500
    )
    return response.choices[0].message["content"].strip()
