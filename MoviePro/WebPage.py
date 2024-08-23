from flask import Flask,request,jsonify,url_for,session,redirect
import requests

from Functions.Recommendations import get_top_50_movies

from Functions.Genres import get_top_3_genres_and_movies
from Functions.Newest import get_newest_10_movies
app = Flask(__name__)
from authlib.integrations.flask_client import OAuth
import os

from dotenv import load_dotenv

def configure():
    load_dotenv()

# API for posters
TMDB_API_KEY = {os.getenv("TMBDapi")}
app.secret_key = 'abc'

def get_movie_poster(movie_title):
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"
    response = requests.get(search_url)
    data = response.json() #returned in json format

    if data['results']:
        poster_path = data['results'][0]['poster_path']
        full_poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        return full_poster_url
    else:
        return "https://via.placeholder.com/150"




@app.route('/')
def index_static():
    movies = get_top_50_movies()

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background-color: #121212;
                color: white;
                overflow-x: hidden;
            }}
            .banner {{
                background-image: url('{url_for("static", filename="pastedimage-xrju-1500w.png")}');
                height: 300px;
                background-size: cover;
                background-position: center;
                margin: 40px auto;
                width: 100%;
                max-width: 1200px;
            }}
            .header {{
                background-color: #1e1e1e;
                padding: 10px 20px;
                text-align: center;
            }}
            .header img {{
                width: 100px;
                height: auto;
                margin-bottom: 10px;
            }}
            .login-btn {{
                margin: 20px 0;
                border: 1px solid white;
                color: white;
                font-size: 1.25rem;
                padding: 10px 20px;
                background-color: #007bff;
                border-radius: 5px;
                text-align: center;
            }}
            .login-btn:hover {{
                background-color: #0056b3;
                color: white;
            }}
            .section-title {{
                text-align: center;
                font-size: 2.5rem;
                margin: 20px 0;
            }}
            .card {{
                position: relative;
                background-color: #2a2a2a;
                border: none;
                transition: transform 0.2s;
                border-radius: 10px;
                overflow: hidden;
                width: 100%;
                max-width: 300px;
            }}
            .card:hover {{
                transform: scale(1.05);
            }}
            .image-container {{
                position: relative;
            }}
            .card-img-top {{
                height: 300px;
                object-fit: cover;
            }}
            .save-movie-btn, .watch-trailer-btn {{
                display: block;
                width: 100%;
                text-align: center;
                padding: 10px;
                color: white;
                background-color: #007bff;
                border: none;
                border-radius: 5px;
                margin-top: 10px;
            }}
            .save-movie-btn:hover, .watch-trailer-btn:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <header class="header">
            <img src="{url_for('static', filename='Film-Reel-Transparent-PNG.png')}" alt="Logo"> 
            <h1>Top Movies Browser</h1>
            <p class="slogan">Your guide to the best films, just a click away!</p>
            <a href="/login" class="btn login-btn">Sign in to Start Browsing</a>
        </header>
        <div class="banner"></div>
        <div class="container mt-5">
            <h1 class="section-title">Our Top Picks</h1>
            <div class="row">
    """

    max_movies = min(len(movies), 50)

    for movie in movies[:max_movies]:
        if len(movie) == 4:
            title, rating, punchline, trailer_url = movie
        else:
            continue

        poster_url = get_movie_poster(title)
        embed_code = f"""
            <p>Login to watch trailer</p>
        """

        html_content += f"""
            <div class="col-md-4 col-sm-6 col-xs-12 mb-4"> 
                <div class="card">
                    <div class="image-container">
                        <img src="{poster_url}" class="card-img-top" alt="{title}">
                    </div>
                    <div class="movie-info">
                        <h5 class="card-title" title="{title}">{title}</h5>
                        <p class="card-text"><strong>Rating:</strong> {rating}</p>
                        <p class="card-text">{punchline}</p>
                    </div>
                    <div class="card-body">
                        {embed_code}
                    </div>
                </div>
            </div>
        """

    html_content += """
            </div>
        </div>
    </body>
    </html>
    """
    return html_content


@app.route('/home')
def home():
    user = dict(session).get('user', None)
    
    saved_movies = session.get('saved_movies', [])

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background-color: #121212;
                color: white;
                overflow-x: hidden;
            }}
            .banner {{
                background-image: url('{url_for("static", filename="pastedimage-xrju-1500w.png")}');
                height: 300px;
                background-size: cover;
                background-position: center;
                margin: 40px auto;
                width: 100%;
                max-width: 1200px;
            }}
            .header {{
                background-color: #1e1e1e;
                padding: 10px 20px;
                text-align: center;
            }}
            .header img {{
                width: 100px;
                height: auto;
                margin-bottom: 10px;
            }}
            .logout-btn {{
                position: absolute;
                right: 20px;
                top: 20px;
                border: 1px solid white;
                color: white;
                font-size: 1.25rem;
                padding: 10px 20px;
            }}
            .section-title {{
                text-align: center;
                font-size: 2.5rem;
                margin: 20px 0;
            }}
            .browse-btn {{
                display: block;
                width: 200px;
                margin: 20px auto;
                padding: 10px;
                font-size: 1.25rem;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                text-align: center;
                text-decoration: none;
            }}
            .browse-btn:hover {{
                background-color: #0056b3;
                color: white;
            }}
            .movie-card {{
                background-color: #2a2a2a;
                border: none;
                border-radius: 15px;
                margin: 15px;
                transition: transform 0.3s;
            }}
            .movie-card:hover {{
                transform: scale(1.05);
            }}
            .card-img-top {{
                max-height: 300px;
                object-fit: cover;
            }}
        </style>
    </head>
    <body>
        <header class="header">
            <img src="{url_for('static', filename='Film-Reel-Transparent-PNG.png')}" alt="Logo"> 
            <h1>Welcome to the Movie Browser</h1>
            <a href="/logout" class="btn logout-btn">Logout</a> 
        </header>
        <div class="banner"></div>
        <div class="container mt-5">
            <h1 class="section-title">Hello, {user['name']}</h1>
            <p class="text-center">You are logged in and ready to explore the best movies!</p>
            <a href="/homebrowsing" class="browse-btn">Start Exploring</a>
        </div>
    </body>
    </html>
    """

    return html_content if user else 'You are not logged in!'


@app.route('/homebrowsing')
def homebrowsing():
    user = dict(session).get('user', None)
    
    if not user:
        return redirect('/login')

    movies = get_top_50_movies()
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background-color: #121212;
                color: white;
                overflow-x: hidden;
            }}
            .banner {{
                background-image: url('{url_for("static", filename="pastedimage-xrju-1500w.png")}');
                height: 300px;
                background-size: cover;
                background-position: center;
                margin: 40px auto;
                width: 100%;
                max-width: 1200px;
            }}
            .header {{
                background-color: #1e1e1e;
                padding: 10px 20px;
                text-align: center;
            }}
            .header img {{
                width: 100px;
                height: auto;
                margin-bottom: 10px;
            }}
            .saved-movies-btn, .logout-btn {{
                margin: 20px 0;
                border: 1px solid white;
                color: white;
                font-size: 1.25rem;
                padding: 10px 20px;
            }}
            .logout-btn {{
                position: absolute;
                right: 20px;
                top: 20px;
            }}
            .card {{
                position: relative;
                background-color: #2a2a2a;
                border: none;
                transition: transform 0.2s;
                border-radius: 10px;
                overflow: hidden;
                width: 100%;
                max-width: 300px;
            }}
            .card:hover {{
                transform: scale(1.05);
            }}
            .image-container {{
                position: relative;
            }}
            .card-img-top {{
                height: 300px;
                object-fit: cover;
            }}
            .save-movie-btn {{
                position: absolute;
                bottom: 10px;
                left: 50%;
                transform: translateX(-50%);
                background-color: rgba(0, 0, 0, 0.99);
                color: white;
                padding: 10px 15px;
                border: 2px solid black;
                border-radius: 5px;
                text-align: center;
                font-size: 1.1rem;
                font-weight: bold;
                transition: background-color 0.3s, border-color 0.3s;
            }}
            .save-movie-btn:hover {{
                background-color: rgba(0, 0, 0, 1);
                border-color: white;
            }}
            .movie-info {{
                padding: 15px;
                text-align: left;
                min-height: 160px;
            }}
            .card-title {{
                font-size: 1.25rem;
                margin: 5px 0;
                white-space: normal;
            }}
            .card-text {{
                font-size: 0.9rem;
            }}
            .btn-primary {{
                background-color: #007bff;
                border: none;
            }}
            .btn-primary:hover {{
                background-color: #0056b3;
            }}
            .row {{
                justify-content: center;
            }}
            .section-title {{
                text-align: center;
                font-size: 2.5rem;
                margin: 20px 0;
            }}
            .slogan {{
                font-size: 1rem;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <header class="header">
            <img src="{url_for('static', filename='Film-Reel-Transparent-PNG.png')}" alt="Logo"> 
            <h1>Top Movies Browser</h1>
            <p class="slogan">Your guide to the best films, just a click away!</p> 
            <a href="/SavedMovies" class="btn saved-movies-btn">Your Saved Movies</a> 
            <a href="/logout" class="btn saved-movies-btn logout-btn">Logout</a> 
        </header>
        <div class="banner"></div>
        <div class="container mt-5">
            <div class="row justify-content-center mb-3">
                <div class="col-auto">
                    <a href="/Newest" class="btn btn-primary">Newest Movies</a>
                </div>
                <div class="col-auto">
                    <a href="/Genres" class="btn btn-primary">Popular Genres</a>
                </div>
            </div>
            <h1 class="section-title">Our Top Picks</h1>
            <div class="row">
    """

    max_movies = min(len(movies), 50)

    for movie in movies[:max_movies]:
        if len(movie) == 4:
            title, rating, punchline, trailer_url = movie
        else:
            continue

        poster_url = get_movie_poster(title)

        if trailer_url:  # Ensure trailer_url is not None
            video_id = trailer_url.split('v=')[-1]
            embed_code = f"""
                <iframe width="100%" height="200"
                        src="https://www.youtube.com/embed/{video_id}"
                        title="YouTube video player"
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                        allowfullscreen>
                </iframe>
            """
        else:
            embed_code = "<p>Trailer not available</p>"

        html_content += f"""
            <div class="col-md-4 col-sm-6 col-xs-12 mb-4"> 
                <div class="card">
                    <div class="image-container">
                        <img src="{poster_url}" class="card-img-top" alt="{title}">
                        <a href="/save_movie?title={title}" class="btn save-movie-btn">Save Movie</a>
                    </div>
                    <div class="movie-info">
                        <h5 class="card-title" title="{title}">{title}</h5>
                        <p class="card-text"><strong>Rating:</strong> {rating}</p>
                        <p class="card-text">{punchline}</p>
                    </div>
                    <div class="card-body">
                        {embed_code}
                    </div>
                </div>
            </div>
        """

    html_content += """
            </div>
        </div>
    </body>
    </html>
    """
    return html_content



@app.route('/save_movie')
def save_movie():
    movie_title = request.args.get('title')

    if 'saved_movies' not in session:
        session['saved_movies'] = []

    session['saved_movies'].append(movie_title)
    session.modified = True
    return redirect('/homebrowsing')

@app.route('/delete_movie')
def delete_movie():
    movie_title = request.args.get('title')

    if 'saved_movies' in session:
        session['saved_movies'] = [movie for movie in session['saved_movies'] if movie != movie_title]
        session.modified = True
    return redirect('/SavedMovies')


@app.route('/SavedMovies')
def get_saved_movies():
    user = session.get('user')
    if not user:
        return redirect('/login')
    
    saved_movies = session.get('saved_movies', [])

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background-color: #121212;
                color: white;
                text-align: center;
                padding: 50px;
            }}
            .movie-card {{
                background-color: #2a2a2a;
                border: none;
                border-radius: 15px;
                margin: 15px;
                transition: transform 0.3s;
            }}
            .movie-card:hover {{
                transform: scale(1.05);
            }}
            .card-img-top {{
                max-height: 300px;
                object-fit: cover;
            }}
            .back-btn {{
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 1.25rem;
                border-radius: 5px;
                text-decoration: none;
            }}
            .back-btn:hover {{
                background-color: #0056b3;
                color: white;
            }}
        </style>
    </head>
    <body>
        <h1>Saved Movies</h1>
        <a href="/homebrowsing" class="btn back-btn" style="margin-top: 20px;">Back to Movies</a>
        <div class="container">
            <div class="row justify-content-center">
    """

    if not saved_movies:
        html_content += "<p>No saved movies yet.</p>"
    else:
        for movie_title in saved_movies:
            poster_url = get_movie_poster(movie_title)
            description = "This is a brief description or punchline for the movie."

            html_content += f"""
                <div class="col-md-3">
                    <div class="card movie-card">
                        <img src="{poster_url}" class="card-img-top" alt="{movie_title}">
                        <div class="card-body">
                            <h5 class="card-title">{movie_title}</h5>
                            <p class="card-text">{description}</p>
                            <a href="/delete_movie?title={movie_title}" class="btn btn-danger">Delete</a>
                        </div>
                    </div>
                </div>
            """

    html_content += """
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

@app.route('/Genres')
def popular_genres():
    user = dict(session).get('user', None)
    
    if not user:
        return redirect('/login')

    genres = get_top_3_genres_and_movies()

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background-color: #121212;
                color: white;
                overflow-x: hidden;
            }}
            .banner {{
                background-image: url('{url_for("static", filename="pastedimage-xrju-1500w.png")}');
                height: 300px;
                background-size: cover;
                background-position: center;
                margin: 40px auto;
                width: 100%;
                max-width: 1200px;
            }}
            .header {{
                background-color: #1e1e1e;
                padding: 10px 20px;
                text-align: center;
            }}
            .header img {{
                width: 100px;
                height: auto;
                margin-bottom: 10px;
            }}
            .saved-movies-btn, .logout-btn {{
                margin: 20px 0;
                border: 1px solid white;
                color: white;
                font-size: 1.25rem;
                padding: 10px 20px;
            }}
            .logout-btn {{
                position: absolute;
                right: 20px;
                top: 20px;
            }}
            .card {{
                position: relative;
                background-color: #2a2a2a;
                border: none;
                transition: transform 0.2s;
                border-radius: 10px;
                overflow: hidden;
                width: 100%;
                max-width: 300px;
            }}
            .card:hover {{
                transform: scale(1.05);
            }}
            .image-container {{
                position: relative;
            }}
            .card-img-top {{
                height: 300px;
                object-fit: cover;
            }}
            .save-movie-btn {{
                position: absolute;
                bottom: 10px;
                left: 50%;
                transform: translateX(-50%);
                background-color: rgba(0, 0, 0, 0.99);
                color: white;
                padding: 10px 15px;
                border: 2px solid black;
                border-radius: 5px;
                text-align: center;
                font-size: 1.1rem;
                font-weight: bold;
                transition: background-color 0.3s, border-color 0.3s;
            }}
            .save-movie-btn:hover {{
                background-color: rgba(0, 0, 0, 1);
                border-color: white;
            }}
            .movie-info {{
                padding: 15px;
                text-align: left;
                min-height: 160px;
            }}
            .card-title {{
                font-size: 1.25rem;
                margin: 5px 0;
                white-space: normal;
            }}
            .card-text {{
                font-size: 0.9rem;
            }}
            .btn-primary {{
                background-color: #007bff;
                border: none;
            }}
            .btn-primary:hover {{
                background-color: #0056b3;
            }}
            .row {{
                justify-content: center;
            }}
            .section-title {{
                text-align: center;
                font-size: 2.5rem;
                margin: 20px 0;
            }}
            .slogan {{
                font-size: 1rem;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <header class="header">
            <img src="{url_for('static', filename='Film-Reel-Transparent-PNG.png')}" alt="Logo"> 
            <h1>Top Movies Browser</h1>
            <p class="slogan">Your guide to the best films, just a click away!</p> 
            <a href="/SavedMovies" class="btn saved-movies-btn">Your Saved Movies</a> 
            <a href="/logout" class="btn saved-movies-btn logout-btn">Logout</a> 
        </header>
        <div class="banner"></div>
        <div class="container mt-5">
            <h1 class="section-title">Top Genres & Their Best Movies</h1>
            <div class="row">
    """

    for genre_info in genres:
        genre_name = genre_info['genre_name']
        avg_rating = genre_info['avg_rating']
        html_content += f"""
            <div class="col-12">
                <h2 class="section-title">Genre: {genre_name} - Average Rating: {avg_rating:.1f}</h2>
            </div>
        """
        for movie in genre_info['movies']:
            title = movie['title']
            year = movie['year']
            rating = movie['rating']
            trailer_url = movie['trailer_url']
            poster_url = get_movie_poster(title)

            video_id = trailer_url.split('v=')[-1]

            html_content += f"""
            <div class="col-md-4 col-sm-6 col-xs-12 mb-4">
                <div class="card">
                    <div class="image-container">
                        <img src="{poster_url}" class="card-img-top" alt="{title}">
                        <a href="/save_movie?title={title}" class="btn save-movie-btn">Save Movie</a>
                    </div>
                    <div class="movie-info">
                        <h5 class="card-title" title="{title}">{title} ({year})</h5>
                        <p class="card-text"><strong>Rating:</strong> {rating}</p>
                    </div>
                    <div class="card-body">
                        <iframe width="100%" height="200"
                                src="https://www.youtube.com/embed/{video_id}"
                                title="YouTube video player"
                                frameborder="0"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                                allowfullscreen>
                        </iframe>
                    </div>
                </div>
            </div>
            """

    html_content += """
            </div>
        </div>
    </body>
    </html>
    """
    return html_content


@app.route('/Newest')
def newest_10_movies():
    user = dict(session).get('user', None)
    
    if not user:
        return redirect('/login')

    try:
        movies = get_newest_10_movies()
        print(movies)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background-color: #121212;
                color: white;
                overflow-x: hidden;
            }}
            .banner {{
                background-image: url('{url_for("static", filename="pastedimage-xrju-1500w.png")}');
                height: 300px;
                background-size: cover;
                background-position: center;
                margin: 40px auto;
                width: 100%;
                max-width: 1200px;
            }}
            .header {{
                background-color: #1e1e1e;
                padding: 10px 20px;
                text-align: center;
            }}
            .header img {{
                width: 100px;
                height: auto;
                margin-bottom: 10px;
            }}
            .saved-movies-btn, .logout-btn {{
                margin: 20px 0;
                border: 1px solid white;
                color: white;
                font-size: 1.25rem;
                padding: 10px 20px;
            }}
            .logout-btn {{
                position: absolute;
                right: 20px;
                top: 20px;
            }}
            .card {{
                position: relative;
                background-color: #2a2a2a;
                border: none;
                transition: transform 0.2s;
                border-radius: 10px;
                overflow: hidden;
                width: 100%;
                max-width: 300px;
            }}
            .card:hover {{
                transform: scale(1.05);
            }}
            .image-container {{
                position: relative;
            }}
            .card-img-top {{
                height: 300px;
                object-fit: cover;
            }}
            .save-movie-btn {{
                position: absolute;
                bottom: 10px;
                left: 50%;
                transform: translateX(-50%);
                background-color: rgba(0, 0, 0, 0.99);
                color: white;
                padding: 10px 15px;
                border: 2px solid black;
                border-radius: 5px;
                text-align: center;
                font-size: 1.1rem;
                font-weight: bold;
                transition: background-color 0.3s, border-color 0.3s;
            }}
            .save-movie-btn:hover {{
                background-color: rgba(0, 0, 0, 1);
                border-color: white;
            }}
            .movie-info {{
                padding: 15px;
                text-align: left;
                min-height: 160px;
            }}
            .card-title {{
                font-size: 1.25rem;
                margin: 5px 0;
                white-space: normal;
            }}
            .card-text {{
                font-size: 0.9rem;
            }}
            .btn-primary {{
                background-color: #007bff;
                border: none;
            }}
            .btn-primary:hover {{
                background-color: #0056b3;
            }}
            .row {{
                justify-content: center;
            }}
            .section-title {{
                text-align: center;
                font-size: 2.5rem;
                margin: 20px 0;
            }}
            .slogan {{
                font-size: 1rem;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <header class="header">
            <img src="{url_for('static', filename='Film-Reel-Transparent-PNG.png')}" alt="Logo"> 
            <h1>Top Movies Browser</h1>
            <p class="slogan">Your guide to the best films, just a click away!</p> 
            <a href="/SavedMovies" class="btn saved-movies-btn">Your Saved Movies</a> 
            <a href="/logout" class="btn saved-movies-btn logout-btn">Logout</a> 
        </header>
        <div class="banner"></div>
        <div class="container mt-5">
            <h1 class="section-title">Newest 10 Movies</h1>
            <div class="row">
    """

    for movie in movies:
        title, year, rating, punchline, trailer_url = movie
        poster_url = get_movie_poster(title)

        video_id = trailer_url.split('v=')[-1]
        
        html_content += f"""
            <div class="col-md-4 col-sm-6 col-xs-12 mb-4"> 
                <div class="card">
                    <div class="image-container">
                        <img src="{poster_url}" class="card-img-top" alt="{title}">
                        <a href="/save_movie?title={title}" class="btn save-movie-btn">Save Movie</a>
                    </div>
                    <div class="movie-info">
                        <h5 class="card-title" title="{title}">{title} ({year})</h5>
                        <p class="card-text"><strong>Rating:</strong> {rating}</p>
                        <p class="card-text">{punchline}</p>
                    </div>
                    <div class="card-body">
                        <iframe width="100%" height="200"
                                src="https://www.youtube.com/embed/{video_id}"
                                title="YouTube video player"
                                frameborder="0"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                                allowfullscreen>
                        </iframe>
                    </div>
                </div>
            </div>
        """

    html_content += """
            </div>
        </div>
    </body>
    </html>
    """
    return html_content










# OAuth Setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='529092675605-47ttf39td12vm1uvks9djjl3ddk39j0m.apps.googleusercontent.com',
    client_secret= {os.getenv("OAUTHkey")},
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'},
)


@app.route('/login')
def login():
    redirect_uri = url_for('callback', _external=True)
    session['nonce'] = os.urandom(24).hex()  # Generate a nonce and store it in the session
    return google.authorize_redirect(redirect_uri, nonce=session['nonce'])


@app.route('/callback')
def callback():
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token, nonce=session['nonce'])  # Pass the nonce when parsing the ID token
    session['user'] = user_info
    return redirect('/home')



@app.route('/logout')
def logout():
    session.pop('user', None)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background-color: #121212;
                color: white;
                overflow-x: hidden;
            }}
            .banner {{
                background-image: url('{url_for("static", filename="pastedimage-xrju-1500w.png")}');
                height: 300px;
                background-size: cover;
                background-position: center;
                margin: 40px auto;
                width: 100%;
                max-width: 1200px;
            }}
            .header {{
                background-color: #1e1e1e;
                padding: 10px 20px;
                text-align: center;
            }}
            .header img {{
                width: 100px;
                height: auto;
                margin-bottom: 10px;
            }}
            .logout-btn {{
                position: absolute;
                right: 20px;
                top: 20px;
                border: 1px solid white;
                color: white;
                font-size: 1.25rem;
                padding: 10px 20px;
            }}
            .section-title {{
                text-align: center;
                font-size: 2.5rem;
                margin: 20px 0;
            }}
            .bye-message {{
                font-size: 1.5rem;
                margin-top: 20px;
            }}
            .tenor-gif-embed {{
                margin-top: 20px;
                width: 100%;  /* Ensure it takes full width of the column */
                height: auto;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
        </style>
    </head>
    <body>
        <header class="header">
            <img src="{url_for('static', filename='Film-Reel-Transparent-PNG.png')}" alt="Logo"> 
            <h1>Thank You for Visiting</h1>
            <p class="slogan">We hope to see you again soon!</p>
            <a href="/login" class="btn logout-btn">Login Again</a>
        </header>
        <div class="banner"></div>
        <div class="container">
            <div class="bye-message">
                <p>Goodbye! You have been logged out.</p>
                <div class="row">
                    <div class="col-md-4">
                        <!-- First Tenor GIF Embed -->
                        <div class="tenor-gif-embed" data-postid="5206258" data-share-method="host" data-aspect-ratio="1.25" data-width="100%">
                            <a href="https://tenor.com/view/in-case-i-dont-see-ya-good-afternoon-good-evening-good-night-the-truman-show-gif-5206258">In Case I Dont See Ya Good Afternoon GIF</a> 
                            from <a href="https://tenor.com/search/in+case+i+dont+see+ya-gifs">In Case I Dont See Ya GIFs</a>
                        </div> 
                        <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
                    </div>
                    <div class="col-md-4">
                        <!-- Second Tenor GIF Embed -->
                        <div class="tenor-gif-embed" data-postid="14498004" data-share-method="host" data-aspect-ratio="1.3278" data-width="100%">
                            <a href="https://tenor.com/view/frodo-hug-sad-crying-hobbit-gif-14498004">Frodo Hug GIF</a> 
                            from <a href="https://tenor.com/search/frodo-gifs">Frodo GIFs</a>
                        </div> 
                        <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
                    </div>
                    <div class="col-md-4">
                        <!-- Third Tenor GIF Embed -->
                        <div class="tenor-gif-embed" data-postid="18770669" data-share-method="host" data-aspect-ratio="1" data-width="100%">
                            <a href="https://tenor.com/view/abell46s-reface-terminator-arnold-hasta-la-vista-beby-gif-18770669">Abell46s Reface GIF</a> 
                            from <a href="https://tenor.com/search/abell46s-gifs">Abell46s GIFs</a>
                        </div> 
                        <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_content
   
    


app.run()
if __name__ == '__main__':
    app.run(debug=True)


