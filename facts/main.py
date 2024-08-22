from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
    )

loader = TextLoader("facts.txt")

docs = loader.load_and_split(
    text_splitter=text_splitter
)

# Chroma = Embeddings, vector search, document storage, full-text search, metadata filtering, and multi-modal. All in one place.

db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="emb"
)

results = db.similarity_search("What is an interesting fact about the English language?", k=1)
# results = db.similarity_search_with_score("What is an interesting fact about the English language?", k=1)

for result in results:
    print("\n")
    print(result.page_content)
    # print(result[1])
    # print(result[0].page_content)

