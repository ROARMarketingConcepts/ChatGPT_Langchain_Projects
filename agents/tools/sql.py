import sqlite3
from langchain.tools import Tool

# Establish connection to SQLite database
conn = sqlite3.connect("db.sqlite")

def list_tables():
    """List all tables in the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cursor.fetchall()   
    return "\n".join([row[0] for row in rows if row[0] is not None])   # return the table names as a string


def run_sqlite_query(query):
    """Execute a SQL query and return the results."""
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.OperationalError as err:     # error handling
        return f"Error executing query: {str(err)}"
    
# Create a Tool for executing SQLite queries.
    
run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="Run a SQLite query on the connected database.",
    func=run_sqlite_query,
)

def describe_tables(table_names):
    """Get the schema of a specific table in the database."""
    cursor = conn.cursor()
    tables = ', '.join("'"+table+ "'" for table in table_names)
    rows = cursor.execute(f"SELECT sql FROM sqlite_master WHERE type= 'table' AND name IN ({tables});")
    return "\n".join([row[0] for row in rows if row[0] is not None])   # return the table names as a stringrows

describe_tables_tool = Tool.from_function(
    name="describe_tables",
    description="Given a list of table names, returns the schema of those tables.",
    func=describe_tables,
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
