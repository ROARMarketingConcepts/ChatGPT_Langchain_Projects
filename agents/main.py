from langchain.chat_models import ChatOpenAI
# from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate,MessagesPlaceholder
from langchain.agents import OpenAIFunctionsAgent,AgentExecutor
from dotenv import load_dotenv
from tools.sql import run_query_tool, list_tables, describe_tables_tool # import the functions from tools/sql.py

load_dotenv()

chat = ChatOpenAI()
tables = list_tables()  # get the list of tables from the database
# print(tables)
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=f"You are an AI that has access to a SQLite database.\n{tables}"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")   # this is where the agent will store intermediate AI assistant                                                      
    ]                                                           # and function messages. It is a scratchpad for the agent.
)

# An agent is a chain that knows how to execute tools.
# It will take a list of tools and convert them into a chain of functions.

agent = OpenAIFunctionsAgent(
    llm=chat,
    tools=[run_query_tool,describe_tables_tool],
    prompt=prompt
    
)

# An agent executor is a function that takes a string and executes it using the agent.
# It runs the agent until the response is not a function call.
# It is essentially a fancy 'while loop' that runs the agent until it is done.

agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=[run_query_tool,describe_tables_tool]
)

agent_executor("How many users have a shipping address?") 