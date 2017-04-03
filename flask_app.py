
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)
app.config["DEBUG"]

comments = []

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('main_page.html', comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))

