import os

DOC_STORE_PATH = "uploaded_docs.txt"

def save_document_text(text: str):
    """Append document text to a local store."""
    with open(DOC_STORE_PATH, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def load_documents():
    """Return all saved document text."""
    if not os.path.exists(DOC_STORE_PATH):
        return ""
    with open(DOC_STORE_PATH, "r", encoding="utf-8") as f:
        return f.read()
