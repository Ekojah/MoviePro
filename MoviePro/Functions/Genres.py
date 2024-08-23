from flask import Flask
import mysql.connector
from mysql.connector import Error

db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'movies',
}
# we want to be able to efficiently allow the queries to be sent into the webpage when called in the main program
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

app = Flask(__name__)


def get_top_3_genres_and_movies():
    try:
        # Establish a database connection
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)

            # Query for top 3 genres with names
            cursor.execute("""
                SELECT g.name as genre_name, mg.genre_id, AVG(m.rating) as avg_rating
                FROM MovieGenres mg
                JOIN movies m ON mg.movie_id = m.id
                JOIN genres g ON mg.genre_id = g.id
                GROUP BY mg.genre_id
                ORDER BY avg_rating DESC
                LIMIT 3;
            """)
            top_genres = cursor.fetchall()

            genres_movies = []

            # Query for top 3 movies within each genre
            for genre in top_genres:
                genre_id = genre['genre_id']

                cursor.execute("""
                    SELECT m.title, m.year, m.rating, m.trailer_url
                    FROM movies m
                    JOIN MovieGenres mg ON m.id = mg.movie_id
                    WHERE mg.genre_id = %s
                    ORDER BY m.rating DESC
                    LIMIT 3;
                """, (genre_id,))

                top_movies = cursor.fetchall()
                genres_movies.append({
                    'genre_name': genre['genre_name'],
                    'avg_rating': genre['avg_rating'],
                    'movies': top_movies
                })

            return genres_movies
        else:
            print("Error: Unable to connect to the database.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()