from pyexpat import model
from sentence_transformers import SentenceTransformer
from sentence_transformers import util

def experiment_with_embeddings():
    model = SentenceTransformer('all-MiniLM-L6-v2')



    sentence1 = "Python is a programming language"
    sentence2 = "Java is a programming language"
    sentence3 = "I love programming in Python!"

    embedding1 = model.encode(sentence1)
    embedding2 = model.encode(sentence2)
    embedding3 = model.encode(sentence3)

    # Calculate cosine similarity
    similarity_score = util.cos_sim(embedding1, embedding3)
    print(f"Similarity between sentence 1 & 3: {similarity_score.item():.4f}")

if __name__ == "__main__":
    experiment_with_embeddings()