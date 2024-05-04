import pandas as pd
from sqlalchemy import create_engine, text

# Define the database connection details for SQL Server Express with Trusted Connection
# Replace 'your_server' and 'your_database' with your actual server and database names
server = 'IT9-JHTFQV2\SQLEXPRESS02'
database_name = 'TrackerDev'
trusted_connection = 'yes'  # Use 'yes' for Trusted Connection

# Construct the connection string with Trusted Connection
connection_string = f"mssql+pyodbc://{server}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"

# Create a database engine
engine = create_engine(connection_string)

# Write your SQL query to update the 'Name' column in the 'Project' table
sql_query = "UPDATE dbo.Project SET Name = 'Chatbrag' WHERE Name = 'Brag';"

# Create a SQLAlchemy text object from the SQL query
sql = text(sql_query)

# Execute the SQL query
with engine.connect() as connection:
    result = connection.execute(sql)

# Print the result
print("Rows affected:", result.rowcount)