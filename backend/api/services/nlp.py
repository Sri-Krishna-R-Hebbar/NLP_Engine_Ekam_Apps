from transformers import pipeline

# Load a free Q&A pipeline (DistilBERT based)
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def ask_model(question, context):
    """
    Uses HuggingFace pipeline to answer from given context (docs).
    """
    if not context or not question:
        return None
    try:
        result = qa_pipeline(question=question, context=context)
        return result["answer"]
    except Exception as e:
        return f"Model error: {str(e)}"
