import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",          # Your MySQL username
        password="NewPassword123!", # Your MySQL password
        database="flask_db"
    )
    return connection
