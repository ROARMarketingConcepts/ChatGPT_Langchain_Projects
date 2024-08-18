from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()
chat = ChatOpenAI()

# set up memory
# 'return messages=True' ensures that all previous messages are stored in HumanMessage objects




memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),    # chat_memory creates a file called 'messages.json in the same directory as this file           
    memory_key="messages",                                  # that stores all previous human and AI messages                      
    return_messages=True,
    llm=chat) 

# Interface to ChatGPT

prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),  # set up messages to be sent to ChatGPT
        HumanMessagePromptTemplate.from_template("{content}"),
    ])
    
chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
    verbose=True
    )    

while True:
    content = input(">> ")
    if content.lower() == "exit":
        break
    elif content.strip() == "":
        print("Please enter some text.")
    else:
        print(f"You said: {content}") 
        result = chain({"content":content}) 
        print(result['text']) 

