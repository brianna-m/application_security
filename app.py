# Brianna Manolopoulos
# Application Security
# Winter 2024 TESC
# https://canvas.evergreen.edu/courses/6279/assignments/111546

from flask import Flask, render_template

app = Flask(__name__, template_folder='')

@app.route('/')
def hello_world(): # put application's code here
    return "Hello World"

@app.route('/index')
def index():
    return render_template(index.html, name='PyCharm')

if __name__ == '__main__':
    app.run()
