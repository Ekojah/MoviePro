
    
</head>
<body>
    <h1>Movie Project (SQL + HTML + PYTHON) Setup Tutorial</h1>
    <p>
        <strong>Genres.py, Recommendations.py, Newest.py</strong> are functions designed to interact with the SQL Database, called in <strong>WebPage.py</strong>.
    </p>
    <p>
        After downloading & running the SQL Database, you'll have to adjust the <code>db.config</code> in Python with your SQL Database User & Password. This is very easy. Just edit the files <strong>Genres.py</strong>, <strong>Newest.py</strong>, and <strong>Recommendations.py</strong>.
    </p>
    <pre>
    db_config = {
        'user': '(your username)',
        'password': '(your password)',
        'host': '(your localhost)',
        'database': 'movies',
    }
    </pre>
    <p>
        Then run <strong>WebPage.py</strong>, right-click on the address displayed to choose your desired browser, and everything will be running.
    </p>
    <h2>What to Install Into Your IDE</h2>
    <p>Run these commands in the terminal:</p>
    <pre>
    pip install flask
    pip install mysql.connector
    pip install oauth
    </pre>
    <h2>Specific Versions & Applications</h2>
    <pre>
    alembic==1.13.2
    Authlib==1.3.1
    blinker==1.8.2
    cachelib==0.13.0
    certifi==2024.7.4
    cffi==1.17.0
    charset-normalizer==3.3.2
    click==8.1.7
    cryptography==43.0.0
    Flask==3.0.3
    Flask-Login==0.6.3
    Flask-Migrate==4.0.7
    Flask-OAuthlib==0.9.6
    Flask-SQLAlchemy==3.1.1
    greenlet==3.0.3
    idna==3.7
    itsdangerous==2.2.0
    Jinja2==3.1.4
    Mako==1.3.5
    MarkupSafe==2.1.5
    mysql-connector-python==9.0.0
    oauthlib==2.1.0
    pycparser==2.22
    requests==2.32.3
    requests-oauthlib==1.1.0
    SQLAlchemy==2.0.32
    typing_extensions==4.12.2
    urllib3==2.2.2
    Werkzeug==3.0.3
    </pre>
</body>
</html>
