# src/document_processor.py
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_bytes):
    """Extracts text from a PDF file in byte format."""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)  # Load the page
        text += page.get_text("text")  # Extract the text
    return text

def process_documents(documents):
    """Processes each document and extracts text."""
    texts = []
    for pdf in documents:
        text = extract_text_from_pdf(pdf)
        texts.append(text)
    return texts
