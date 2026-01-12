
def create_qa_prompt(question: str, context: str) -> str:
    prompt3 = f"""
    Answer the question based only on the material provided, if you can't find related
    information in the context, say "I can't find the information in material provided".
    
    Context: {context}
    Question: {question}
    Answer:
    """
    return prompt3 