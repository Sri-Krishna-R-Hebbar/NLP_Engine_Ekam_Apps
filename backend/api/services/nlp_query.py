from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline

class NLPQueryEngine:
    def __init__(self, document_processor):
        self.doc_service = document_processor
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    def answer(self, query):
        # Step 1 — Search documents
        doc_matches = self.doc_service.search(query, top_k=5)

        # Step 2 — Combine documents into one context
        context = " ".join(doc_matches)

        print("[NLPQueryEngine] Context:", context)
        print("[NLPQueryEngine] Query:", query)

        # Step 3 — Ask the model
        if context.strip() == "":
            return "No relevant documents found."
        
        try:
            answer = self.qa_pipeline(question=query, context=context)
            print("[NLPQueryEngine] Model answer:", answer)
            return answer["answer"]
        except Exception as e:
            print("[NLPQueryEngine] QA error:", str(e))
            return "Could not generate answer."
