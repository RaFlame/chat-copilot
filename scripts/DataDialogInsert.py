import pyodbc

# Replace 'your_server' and 'your_database' with your SQL Server Express server and database information
connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=IT9-JHTFQV2\SQLEXPRESS02;' \
    'DATABASE=TrackerDev;' \
    'Trusted_Connection=yes;'
)

cursor = connection.cursor()

cursor.execute(
    """
    UPDATE dbo.Project
    SET Name = 'Brag'
    WHERE Name = 'Chatbrag';

""")

# Commit the changes and close the connection
connection.commit()
connection.close()