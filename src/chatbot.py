# src/chatbot.py
from openai import OpenAI
from config import OPENAI_API_KEY
from chroma_retrieval import retrieve_relevant_content
import chromadb

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_answer_from_retrieved_content(query, relevant_documents):
    """Generate an answer from the retrieved content and the query."""
    # Flatten the list of lists into a single list of strings
    flattened_documents = [doc for sublist in relevant_documents for doc in sublist]

    # Combine the retrieved content into a single context
    context = " ".join(flattened_documents)

    # Use OpenAI's ChatCompletion API to generate an answer
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can use GPT-4 if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on provided context."},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error occurred: {e}"

def get_answer(query):
    """Main function to retrieve content and generate an answer based on the query."""
    # Initialize Chroma client
    client = chromadb.Client()

    # Get or create the collection
    try:
        collection = client.get_collection(name="lecture_notes")
    except chromadb.errors.InvalidCollectionException:
        collection = client.create_collection(name="lecture_notes")

    # Step 1: Retrieve relevant documents from Chroma based on the query
    relevant_documents = retrieve_relevant_content(query, collection)

    # Step 2: Generate an answer based on the retrieved documents
    answer = generate_answer_from_retrieved_content(query, relevant_documents)

    return answer
