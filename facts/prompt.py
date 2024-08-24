from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from redundant_filter_retriever import RedundantFilterRetriever
import langchain
from dotenv import load_dotenv

langchain.debug = True # Turn debug mode on.

load_dotenv()

chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)
# retriever = db.as_retriever()     # the retreiver object has to have some sort of method called "get_relevant_documents"  
                                    # It is the 'glue' between the chain and the db.
                                
retriever = RedundantFilterRetriever(
    embeddings=embeddings, 
    chroma=db)

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff"   # 'stuff' retrievals from the vector store into the SystemMessagePrompt
)

result = chain.run("What is an interesting fact about the English language?")

print(result)
