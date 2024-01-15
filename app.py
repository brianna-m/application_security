# Brianna Manolopoulos
# Application Security
# Winter 2024 TESC
# https://canvas.evergreen.edu/courses/6279/assignments/111546

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='./templates',  static_folder='./static')

@app.route('/')
def home(): # Task 4, Item 1
    return render_template('index.html', name='not_sure_what_this_name_is_for')

@app.route('/index')
def index():
    return render_template('index.html', name='PyCharm')

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        user_input = request.form['w1_input']
        return render_template('submission_result.html', user_input=user_input)

if __name__ == '__main__':
    app.run()
