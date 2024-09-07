import os
import pinecone
from langchain.vectorstores.pinecone import Pinecone
from app.chat.embeddings.openai import embeddings

# Initialize Pinecone

pinecone.Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment = os.getenv("PINECONE_ENV_NAME")    
)

# Create a Pinecone vector store

vector_store = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"), embeddings
)