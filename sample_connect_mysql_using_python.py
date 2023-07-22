import mysql.connector

# Replace the following values with your MySQL database credentials
host = 'your_host'
user = 'your_username'
password = 'your_password'
database = 'your_database_name'

try:
    # Establish the connection
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database successfully!")

    # Perform database operations here (e.g., execute queries, insert data, etc.)
    cursor=connection.cursor()
    cursor.execute("SHOW TABLES")
    for table_name in cursor:
        print(table_name)

except mysql.connector.Error as e:
    print("Error while connecting to MySQL database:", e)

finally:
    # Close the database connection when done
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL database connection closed.")