import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='192.168.0.83',
                            database='work_db',
                            user='postgres',
                            password='123')
                            #user=os.environ['DB_USERNAME'], #можно заменить просто на имя юзера 
                                                            #было сделано с помощью export DB_USERNAME="pstgres"
                            #password=os.environ['DB_PASSWORD']) #можно заменить просто на пароль 
                                                            #было сделано с помощью export DB_PASSWORD="123"
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall() #возвращает список всех строк
    cur.close()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)', #можно было просто написать (VALUES(title, author, pages_num, review))
                    (title, author, pages_num, review))
        conn.commit() #применение изменений 
        cur.close()   
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')