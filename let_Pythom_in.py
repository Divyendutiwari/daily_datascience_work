from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def welcome():
    return "<h1>welcome to lask</h1>"
@app.route('/index')
def index():
    return render_template('D:\\anaconda program\\flask framework\\form.html')
@app.route('/hello')
def about():
    return "<h1>hello world</h1>"
if __name__=="__main__":
    app.run(debug=True)