# src/test_loader.py
from document_loader import download_lecture_notes

def test_download():
    documents = download_lecture_notes()
    print(f"Downloaded {len(documents)} documents.")

if __name__ == "__main__":
    test_download()
