from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/yoga')
def hello_yoga():
    return redirect('/')


@app.route('/menu')
def hello_menu():
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.run(debug=True)
