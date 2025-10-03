from transformers import pipeline

# Load a small free model from HuggingFace
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_from_documents(question: str, context: str):
    """Return answer from documents using HuggingFace QA model."""
    if not context.strip():
        return "No relevant documents available."
    try:
        result = qa_pipeline(question=question, context=context)
        return result["answer"]
    except Exception as e:
        return f"Model error: {str(e)}"
