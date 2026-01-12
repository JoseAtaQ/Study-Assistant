def test_prompts():
    from ai_interface import AIInterface
    
    ai = AIInterface()
    
    context = """
    Binary search is an efficient algorithm for finding an item from a sorted list.
    It works by repeatedly dividing the search interval in half.
    Time complexity is O(log n).
    """
    
    question = "What is binary search?"
    
    # Prompt 1: Direct
    prompt1 = f"{question}"
    
    # Prompt 2: With context
    prompt2 = f"Context: {context}\n\nQuestion: {question}"
    
    # Prompt 3: With instructions
    prompt3 = f"""
    Answer the question based only on the provided context.
    
    Context: {context}
    Question: {question}
    Answer:
    """
    

    print("Testing different prompts...\n")
    for i, prompt in enumerate([prompt1, prompt2, prompt3], 1):
        print(f"Prompt {i}:")
        response = ai.chat(prompt)
        print(f"Response: {response[:200]}...\n")
        print("-" * 60)
    

if __name__ == "__main__":
    test_prompts()