from flask import Flask, render_template, request
from requests import get
app= Flask(__name__)
@app.route('/')
def welcome():
    return render_template('extract.html')
@app.route('/greet')
def greet():
    name: str = request.args.get('name', 'User')
    return f"Hello, {name}! Welcome to the Flask Web App!"
if __name__ == '__main__':
    app.run(debug=True)
