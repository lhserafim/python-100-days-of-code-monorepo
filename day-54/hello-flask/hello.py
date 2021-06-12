# https://flask.palletsprojects.com/en/1.1.x/quickstart/
from flask import Flask
from markupsafe import escape

app = Flask(__name__)  # __name__ é um atributo especial do python, assim como __main__, __dict__, __class__


# criando decorators
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


# criando decorators
def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


# criando decorators
def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route('/')  # Python decorator. Decorators "adicionam" funcionalidades a uma function
def hello_world():
    return '<h1 style="text-align: center" >Hello, World!</h1>' \
           '<p> paragraph </p>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"


# https://flask.palletsprojects.com/en/1.1.x/quickstart/
@app.route("/username/<name>")
def greeting(name):
    return f"Hello {name}"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


# To run the application you can either use the flask command or python’s -m switch with Flask.
# Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP
# environment variable:
#
# $ export FLASK_APP=hello.py
# $ flask run
#  * Running on http://127.0.0.1:5000/

# Também posso rodar minha aplicação utilizando a validação do __name__ abaixo
print(__name__)
if __name__ == "__main__":
    app.run(debug=True)  # o modo debug auxilia e permite fazer refresh automaticamente na página
