from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

class DocumentStore:
    #initialise vector store
    def __init__(self, collection_name: str = "study_docs"):
        self.embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_store = Chroma(
            collection_name=collection_name,
            embedding_function=self.embeddings_model
        )
    
    #add documents to vector store
    def add_documents(self, texts: list[str], metadata: list[dict] = None):
        self.vector_store.add_texts(texts=texts, metadatas=metadata)

    #find the most revelant chunks
    def search(self, query: str, top_k: int = 3) -> list[str]:
        results = self.vector_store.similarity_search(query, k=top_k)
        return [result.page_content for result in results]
    
    #clear the vector store
    def clear(self):
        self.vector_store.delete_collection()

if __name__ == "__main__":
        store = DocumentStore()
        
        # Test documents
        docs = [
            "Python is a high-level programming language",
            "Java is used for enterprise applications",
            "The sky appears blue due to Rayleigh scattering"
        ]
        
        print("Adding documents...")
        store.add_documents(docs)
        
        print("\nSearching for 'programming'...")
        results = store.search("programming languages", top_k=2)
        print("Results:", results)
        
        print("\nSearching for 'color of sky'...")
        results = store.search("why is sky blue", top_k=1)
        print("Results:", results)    