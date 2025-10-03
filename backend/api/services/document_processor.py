import os
from transformers import pipeline
from PyPDF2 import PdfReader

class DocumentProcessor:
    def __init__(self):
        # HuggingFace DistilBERT QA model
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
        self.documents = ""
        self.upload_folder = "uploads"
        os.makedirs(self.upload_folder, exist_ok=True)

    def process_documents(self, file_paths):
        text_content = []

        for path in file_paths:
            if path.endswith(".txt"):
                with open(path, "r", encoding="utf-8") as f:
                    text_content.append(f.read())

            elif path.endswith(".pdf"):
                try:
                    reader = PdfReader(path)
                    for page in reader.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text_content.append(page_text.strip())
                except Exception as e:
                    text_content.append(f"[Error reading PDF {path}: {str(e)}]")

            elif path.endswith(".docx"):
                try:
                    import docx
                    doc = docx.Document(path)
                    for para in doc.paragraphs:
                        if para.text:
                            text_content.append(para.text.strip())
                except Exception as e:
                    text_content.append(f"[Error reading DOCX {path}: {str(e)}]")

        # Join all text and store in memory
        self.documents = "\n".join(filter(None, text_content)).strip()

        # Save to disk for persistence
        with open(os.path.join(self.upload_folder, "uploaded_docs.txt"), "w", encoding="utf-8") as f:
            f.write(self.documents if self.documents else "EMPTY")

    def query_documents(self, question: str):
        # Reload document if not in memory
        if not self.documents:
            try:
                with open(os.path.join(self.upload_folder, "uploaded_docs.txt"), "r", encoding="utf-8") as f:
                    self.documents = f.read().strip()
            except FileNotFoundError:
                return "No documents uploaded yet."

        if not self.documents or self.documents == "EMPTY":
            return "No documents uploaded yet."

        try:
            result = self.qa_pipeline(question=question, context=self.documents)
            return result.get("answer", "No relevant answer found.")
        except Exception as e:
            return f"Error in document QA: {str(e)}"
