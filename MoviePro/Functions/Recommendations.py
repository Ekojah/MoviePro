from flask import Flask
import mysql.connector
from mysql.connector import Error

db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'movies',
}

app = Flask(__name__)

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

def get_top_50_movies():
    try:
        sqlQuery = "SELECT title, rating, punchline, trailer_url FROM movies ORDER BY rating DESC LIMIT 50"
        cursor.execute(sqlQuery)
        res = cursor.fetchall()
        return res
    except Error as e:
        print(f"Error: {e}")
        return []


