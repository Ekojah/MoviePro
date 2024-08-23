from flask import Flask
import mysql.connector
from mysql.connector import Error

db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'movies',
}
#we want to be able to efficiently allow the queries to be sent into the webpage when called in the main program
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

app = Flask(__name__)

def get_newest_10_movies():
    try:
        # Establish a database connection
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            cursor = conn.cursor()
            # SQL query to fetch the 10 newest movies by year
            sqlQuery = "SELECT title, year, rating, punchline, trailer_url FROM movies ORDER BY year DESC LIMIT 10"
            cursor.execute(sqlQuery)
            # Fetch the results
            res = cursor.fetchall()
            return res
        else:
            print("Error: Unable to connect to the database.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()