# src/test_text_extraction.py
from document_loader import download_lecture_notes
from document_processor import process_documents

def test_extract_text():
    documents = download_lecture_notes()  # Download PDFs
    extracted_texts = process_documents(documents)  # Extract text from PDFs
    assert len(extracted_texts) > 0, "No text was extracted from PDFs!"
    
    for i, text in enumerate(extracted_texts):
        print(f"PDF {i+1} Extracted Text (first 500 characters):\n{text[:500]}\n")

if __name__ == "__main__":
    test_extract_text()
