Study Assistant
A privacy-focused, local AI CLI tool Works as a chatbot, but it's primarily designed to receive a document (PDF) that serves as the context for subsequent questions. Built using Retrieval-Augmented Generation (RAG), this assistant ensures your data never leaves your machine.

This project implements a full RAG pipeline from scratch to bridge the gap between static documents and generative AI.

1. Document Ingestion Pipeline
Extraction: Uses PyMuPDF to parse and clean text from PDF documents.

Semantic Chunking: Instead of arbitrary character limits, text is split into meaningful segments using langchain-experimental's Semantic Chunker, ensuring context is preserved.

Vector Embeddings: Each chunk is transformed into a 384-dimensional vector using the all-MiniLM-L6-v2 transformer model.

2. Intelligent Storage & Retrieval
Vector Database: Powered by ChromaDB for high-performance similarity searches.

Semantic Search: When a user asks a question, the system performs a mathematical similarity check to retrieve the top-K most relevant document "chunks" rather than just matching keywords.

3. Local Generation (Ollama)
Privacy-First AI: Leverages Ollama to run Llama 2 (or other GGUF models) locally.

Augmented Prompting: The system constructs a specialized prompt containing the retrieved context, forcing the AI to answer based on your specific notes rather than general training data.


Requirements & Setup
Ollama: Install Ollama and ensure the service is running.

Model: By default, this tool uses llama2. If the model is not found, the program will attempt to pull it automatically on the first run. The program can also directly install any other Ollama agent you like(make sure you write the exact model and version).
