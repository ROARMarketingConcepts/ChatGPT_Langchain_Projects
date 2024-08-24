from langchain.embeddings.base import Embeddings
from langchain.vectorstores import Chroma
from langchain.schema import BaseRetriever


class RedundantFilterRetriever(BaseRetriever):
    embeddings:Embeddings 
    chroma:Chroma  

    def get_relevant_documents(self, query):
        # Embed the query
        emb = self.embeddings.embed_query(query)
        
        # Feed embeddings to max_marginal_relevance_search_by_vector
        
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding = emb, 
            lambda_mult = 0.8)
    
    async def aget_relevant_documents(self):
        return
