# src/langchain_integration.py
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import os

# Load your OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize LangChain's OpenAI embeddings and Chroma
def initialize_chroma():
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    db = Chroma(embedding_function=embeddings)
    return db

# Ingest a PDF document into Chroma using LangChain
def ingest_documents_to_chroma(pdf_paths):
    db = initialize_chroma()

    for pdf_path in pdf_paths:
        loader = PyMuPDFLoader(pdf_path)
        documents = loader.load()
        db.add_documents(documents)
        print(f"Ingested {pdf_path}")

# Use LangChain's retrieval-based QA chain for querying documents
def query_documents(query):
    db = initialize_chroma()
    llm = OpenAI(openai_api_key=openai_api_key)
    chain = load_qa_chain(llm, chain_type="stuff")
    
    # Query Chroma for the most relevant documents
    relevant_docs = db.similarity_search(query, k=3)

    # Generate an answer using the QA chain
    answer = chain.run(input_documents=relevant_docs, question=query)
    return answer
