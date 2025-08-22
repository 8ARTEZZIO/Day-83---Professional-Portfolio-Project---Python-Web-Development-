from flask import Flask, url_for, request, render_template
import datetime

app = Flask(__name__)

year = datetime.date.today().year

@app.route("/")
def home():
    global year
    return render_template('index.html', year=year)

@app.route('/projects/')
def projects():
    return render_template('projects.html', year=year)

@app.route('/about')
def about():
    return render_template('about.html', year=year)

if __name__ == "__main__":
    app.run(port=8000, debug=True)