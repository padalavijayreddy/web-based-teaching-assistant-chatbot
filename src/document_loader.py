# src/document_loader.py
import requests

def download_lecture_notes():
    """Downloads lecture notes from a list of URLs and returns a list of PDFs in byte format."""
    lecture_urls = [
        "https://inst.eecs.berkeley.edu/~cs188/su24/assets/lectures/cs188-su24-lec01.pdf",
        "https://inst.eecs.berkeley.edu/~cs188/su24/assets/lectures/cs188-su24-lec02.pdf",
        "https://inst.eecs.berkeley.edu/~cs188/su24/assets/lectures/cs188-su24-lec03.pdf",
        "https://inst.eecs.berkeley.edu/~cs188/su24/assets/lectures/cs188-su24-lec04.pdf",
        "https://inst.eecs.berkeley.edu/~cs188/su24/assets/lectures/cs188-su24-lec05.pdf",
        # Add more URLs here if needed
    ]

    documents = []
    for url in lecture_urls:
        response = requests.get(url)
        if response.status_code == 200:
            documents.append(response.content)
            print(f"Successfully downloaded {url}")
        else:
            print(f"Failed to download {url} (status code {response.status_code})")
    return documents
