# src/test_embeddings.py
from document_loader import download_lecture_notes
from document_processor import process_documents
from embeddings import generate_embeddings

def test_generate_embeddings():
    documents = download_lecture_notes()  # Download PDFs
    extracted_texts = process_documents(documents)  # Extract text from PDFs
    embeddings = generate_embeddings(extracted_texts)  # Generate embeddings
    
    assert len(embeddings) == len(extracted_texts), "Mismatch between embeddings and extracted texts!"
    print(f"Generated {len(embeddings)} embeddings successfully.")

if __name__ == "__main__":
    test_generate_embeddings()
