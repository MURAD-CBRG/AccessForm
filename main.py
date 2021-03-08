from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def start_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index_page():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion_page():
    return '''
    Человечество вырастает из детства.<br>
    Человечеству мала одна планета.<br>
    Мы сделаем обитаемыми безжизненные пока планеты.<br>
    И начнем с Марса!<br>
    Присоединяйся!
    '''


@app.route('/image_mars')
def image_mars_page():
    return '''
    <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src="static\MARS.png">
    <p>Mars Planet</p>
    '''


@app.route('/promotion_page')
def promotion_page_pro():
    code = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Колонизация</title>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/designer.css')}">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
        </head>
        <body>

            <h1 id='header_text'>Жди нас, Марс</h1>

            <img src="static/img/MARS.PNG">
            <p>Planet Mars</p><br>

            <span style="margin: 10%; width="90%">
                
                <p class="alert alert-danger">Человечество вырастает из детства.</p>
                <p class="alert alert-info">Человечеству мала одна планета.</p>
                <p class="alert alert-dark">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                <p class="alert alert-warning">И начнем с Марса!</p>
                <p class="alert alert-success">Присоединяйся!</p>

            </span>


        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
        </body>
        </html>
    '''

    return code


if __name__ == '__main__':
    app.run(port=8080, host='localhost')
