import os
import re
import fitz
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Clean text function
def clean_text(text: str) -> str:
    text = re.sub(r'Page \d+( of \d+)?', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Remove non-ascii characters
    text = text.encode("ascii", "ignore").decode()
    
    return text.strip()

# Extract text from PDF
# Extract text and keep metadata per page
def extract_text_from_pdf_with_metadata(pdf_path: str) -> list[dict]:
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The file at {pdf_path} was not found.")
    
    pages_data = []
    try:
        with fitz.open(pdf_path) as doc:
            for page_num, page in enumerate(doc):
                raw_text = page.get_text()
                cleaned_text = clean_text(raw_text)
                
                if cleaned_text: # Only add if there is actual text
                    pages_data.append({
                        "text": cleaned_text,
                        "metadata": {
                            "source": os.path.basename(pdf_path),
                            "page": page_num + 1
                        }
                    })
    except Exception as e:
        raise RuntimeError(f"Failed to read PDF: {e}")
    return pages_data

# Perform semantic chunking
def semantic_chunking_with_metadata(pages_data: list[dict]) -> tuple[list[str], list[dict]]:
    chunker = SemanticChunker(
        embeddings_model,
        breakpoint_threshold_type='percentile',
        breakpoint_threshold_amount=90
    )
    
    all_chunks = []
    all_metadatas = []
    
    for page in pages_data:
        # Split the text of this specific page
        chunks = chunker.split_text(page["text"])
        for chunk in chunks:
            all_chunks.append(chunk)
            # Attach the page's metadata to every chunk created from that page
            all_metadatas.append(page["metadata"])
            
    return all_chunks, all_metadatas

if __name__ == "__main__":
    file_path = "Resume (1).pdf"
    pages_data = extract_text_from_pdf_with_metadata(file_path)
    chunks, metadatas = semantic_chunking_with_metadata(pages_data)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:\n{chunk}\n{'-'*40}\n")



        