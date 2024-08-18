from langchain.document_loaders import TextLoader
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import LLMChain
# from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
# from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("facts.txt")
docs = loader.load()

print(docs)
