
def create_qa_prompt(question: str, context: str) -> str:
    if not context.strip():
        # If no document is loaded, just send the question directly
        return f"Question: {question}\nAnswer the user's question directly."
    
    # If a document is loaded
    return f"""
    Context from notes: {context}
    
    Question: {question}
    
    Instructions: Answer the question using the provided context. If the answer 
    isn't in the context, you may use your general knowledge, but clearly state 
    when you are doing so.
    """