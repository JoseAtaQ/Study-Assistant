from pdf_processor import extract_text_from_pdf_with_metadata, semantic_chunking_with_metadata
from vector_store import DocumentStore
from ai_interface import AIInterface
from prompt_templates import create_qa_prompt

class StudyAssistant:
    """
    Main class that coordinates everything.
    """
    
    def __init__(self, model_name: str = "llama2"):
        self.document_store = DocumentStore()
        self.ai_interface = AIInterface(model_name=model_name)
        self.chat_history = []
        self.is_initialized = True
    
    def load_pdf(self, pdf_path: str) -> bool:
        try:
            pages_data = extract_text_from_pdf_with_metadata(pdf_path)
            
            chunks, metadatas = semantic_chunking_with_metadata(pages_data)
            
            self.document_store.add_documents(chunks, metadatas)
            return True
        except Exception as e:
            print(f"Error loading PDF: {e}")
        return False
    
    def ask(self, question: str) -> str:
        if not question.strip():
            return "Please provide a valid question."
        relevant_contexts = self.document_store.search(question, top_k=3)
        combined_context = "\n\n".join(relevant_contexts)
        prompt = create_qa_prompt(question, combined_context)

        response = self.ai_interface.chat(prompt)
        self.chat_history.append((question, response))
        return response
    
if __name__ == "__main__":
    print("Testing Study Assistant...\n")
    
    assistant = StudyAssistant()
    
    # Load PDF
    print("Test 1: Loading PDF...")
    success = assistant.load_pdf("Resume (1).pdf")
    print(f"Result: {'Success' if success else 'Failed'}\n")
    
    # Ask question
    print("Test 2: Asking question...")
    answer = assistant.ask("What is the main topic of this document?")
    print(f"Answer: {answer}\n")

    # Error handling
    print("Test 4: Testing error handling...")
    answer = assistant.ask("")  # Empty question
    print(f"Empty question response: {answer}\n")