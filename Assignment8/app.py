from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('cv.html')


@app.route('/ContactList')
def contact_list():
    return render_template('Contact List.html')


@app.route('/assignement8')
def assignement8_func():
    user_1 = {'firstName': 'Gaia', 'lastName': 'Tamir', 'gender': 'female'}
    return render_template('assignment8.html', user=user_1, hobbies=['yoga', 'running', 'beaching'])


if __name__ == '__main__':
    app.run(debug=True)