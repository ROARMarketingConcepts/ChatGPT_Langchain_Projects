from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate,MessagesPlaceholder
from langchain.agents import OpenAIFunctionsAgent,AgentExecutor
from dotenv import load_dotenv
from tools.sql import run_query_tool

load_dotenv()

chat = ChatOpenAI()
prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

agent = OpenAIFunctionsAgent(
    llm=chat,
    tools=[run_query_tool],
    prompt=prompt
    
)

agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=[run_query_tool]
)

agent_executor("How many users are there in the database?") 