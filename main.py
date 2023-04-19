from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def mars():
    return "Миссия Колонизация Марса"


@app.route('/index')
def apple():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return f"Человечество вырастает из детства.</br></br>" \
           f"Человечеству мала одна планета.</br></br>" \
           f"Мы сделаем обитаемыми безжизненные пока планеты.</br></br>" \
           f"И начнем с Марса!</br></br>" \
           f"Присоединяйся!"


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                      </body>
                      <img src="{url_for('static', filename='img/mars.png')}" 
                      alt="здесь должна была быть картинка, но не нашлась">
                      <body>
                        <br><h>Вот она какая, красная планета.</h>
                    </html>"""


@app.route('/promotion_image')
def bootstrap():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <h1>Жди нас, Марс!</h1>
                  </body>
                  <img src="{url_for('static', filename='img/mars.png')}" alt="альтернативный текст">
                  <body>
                    <div class="alert alert-dark" role="alert">
                      <strong>Человечество вырастет из детства.</strong>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <strong>Человечеству мала одна планета.</strong>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      <strong>Мы сделаем обитаемыми безжизненные пока планеты.</strong>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <strong>И начнём с Марса!</strong>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <strong>Присоединяйся!</strong>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
