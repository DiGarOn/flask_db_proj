from flask import Flask, render_template
import psycopg2
from werkzeug.exceptions import abort
from config import host, user, password, db_name

def get_db_connection():
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    return connection
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

