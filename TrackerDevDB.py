import pyodbc

def connect_to_sql_server(database_name, server_name='localhost\\SQLEXPRESS02'):
    """
    Connect to an internal SQL Server Express database using Windows Authentication.

    Parameters:
    - database_name: The name of the database to connect to.
    - server_name: The name of the SQL Server instance, defaulting to 'localhost\\SQLEXPRESS02'.
    
    Returns:
    - A connection object that can be used for executing queries.
    """
    try:
        # Create a connection string using Windows Authentication
        conn_str = f'DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes;'
        
        # Establish a connection to the database
        conn = pyodbc.connect(conn_str)
        print("Connection successful!")
        return conn
    except Exception as e:
        print("Error connecting to SQL Server Express:", e)
        return None

# Example usage
database_name = 'TrackerDev'  # Replace with your database name
server_name = 'localhost\\SQLEXPRESS02'  # Adjust as needed, or leave as default for local SQLEXPRESS

conn = connect_to_sql_server(database_name, server_name)

if conn:
    # You can now use `conn` to execute queries against your database.
    pass