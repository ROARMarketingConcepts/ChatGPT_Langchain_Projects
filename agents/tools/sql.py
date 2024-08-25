import sqlite3
from langchain.tools import Tool

# Establish connection to SQLite database
conn = sqlite3.connect("db.sqlite")


def run_sqlite_query(query):
    """Execute a SQL query and return the results."""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Create a Tool for executing SQLite queries.
    
run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="Run a SQLite query on the connected database.",
    func=run_sqlite_query,
)

# # Create a Tool for getting table names
# get_tables_tool = Tool(
#     name="Get Table Names",
#     func=get_table_names,
#     description="Get a list of all table names in the database."
# )

# # Create a Tool for getting table schema
# get_schema_tool = Tool(
#     name="Get Table Schema",
#     func=get_table_schema,
#     description="Get the schema of a specific table in the database."
# )
