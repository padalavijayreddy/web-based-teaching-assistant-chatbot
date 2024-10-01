# src/test_document_extraction.py
from document_loader import download_lecture_notes
from document_processor import process_documents

def test_document_extraction():
    documents = download_lecture_notes()  # Download PDFs
    assert len(documents) > 0, "No documents were downloaded!"
    print(f"Downloaded {len(documents)} lecture notes.")

    extracted_texts = process_documents(documents)  # Extract text from PDFs
    assert len(extracted_texts) > 0, "No text was extracted from the documents!"
    
    # Print the first 500 characters of the first extracted document
    print(f"Extracted text from the first document: {extracted_texts[0][:500]}")

if __name__ == "__main__":
    test_document_extraction()
