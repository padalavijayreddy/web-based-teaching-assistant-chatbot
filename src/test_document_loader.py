# src/test_document_loader.py
from document_loader import download_lecture_notes

def test_download_lecture_notes():
    documents = download_lecture_notes()  # Download PDFs
    assert len(documents) > 0, "No documents were downloaded!"
    print(f"Downloaded {len(documents)} lecture notes successfully.")

if __name__ == "__main__":
    test_download_lecture_notes()
