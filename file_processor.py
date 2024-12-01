import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using pdfplumber.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def clean_text(text):
    """
    Cleans the extracted text by removing extra spaces, page numbers, headers, and footers.
    """
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'Page \d+|Header text|Footer text', '', text)  # Remove page numbers, headers, and footers
    return text.strip()

