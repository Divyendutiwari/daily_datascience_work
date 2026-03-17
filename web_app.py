from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def welcome():
    return "Welcome to the Flask Web App!"
@app.route('/greet')
def greet():
    return "Hello, User! Welcome to the Flask Web App!"
if __name__ == '__main__':
    app.run(debug=True)
