
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, redirect, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"]

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
            username="opeker",
            password="gbolojo23db",
            hostname="opeker.mysql.pythonanywhere-services.com",
            databasename="opeker$comments",)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)

comments = []

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('main_page.html', comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))

