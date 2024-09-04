from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

from tools.sql import run_query_tool, list_tables, describe_tables_tool
from tools.report import write_report_tool
from handlers.chat_model_start_handler import ChatModelStartHandler

load_dotenv()

handler = ChatModelStartHandler()
chat = ChatOpenAI(
    callbacks=[handler]
)

tables = list_tables()    # get the list of tables from the database

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=(
            "You are an AI that has access to a SQLite database.\n\n"
            f"The database has tables of:\n{tables}\n"
            "\n\nDo not make any assumptions about what tables exist "
            "or what columns exist. Instead, use the 'describe_tables' function"
        )),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")   # this is where the agent will store intermediate AI assistant  
    ]                                                           # and function messages. It is a scratchpad for the agent.
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# The list of tools that we will be using to interact with the AI host.

tools = [
    run_query_tool,
    describe_tables_tool,
    write_report_tool
]

agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)
# An agent executor is a function that takes a string and executes it using the agent.
# It runs the agent until the response is not a function call.
# It is essentially a fancy 'while loop' that runs the agent until it is done.

agent_executor = AgentExecutor(
    agent=agent,
    # verbose=True,
    tools=tools,
    memory=memory
)

agent_executor(
    "How many orders are there? Write the result to an html report."
)

agent_executor(
    "Repeat the exact same process for users."
)

agent_executor(
    "What is the average number of products per order?"
)

agent_executor(
    "How many products have a price that is higher than the average product price?"
)