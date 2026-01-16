Study Assistant

Works as a chatbot, but it's primarily designed to receive a document (PDF) that serves as the context for subsequent questions.
This project uses Retrieval-Augmented Generation (RAG), which combines 
document search with AI text generation:

1. Document Processing
   - PDFs are uploaded, and text is extracted
   - Text is split into chunks of ~500 words
   - Each chunk is converted to a vector embedding using [all-MiniLM-L6-v2]

2. Storage
   - Embeddings are stored in [ChromaDB]
   - Allows semantic search (meaning-based, not keyword-based)

3. Question Answering
   - When you ask a question:
     a. Your question is converted to an embedding
     b. Similar chunks are retrieved from the database
     c. Relevant chunks are sent to Ollama as context
     d. Ollama generates an answer based only on that context

**Before using it, you will need Ollama installed and running. The program can also install any agent if you don't have it(make sure you write the exact model and version)**
