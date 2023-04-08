from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return render_template('./index.html')


@app.route('/blog')
def blog():
    return "<p>These are my thoughts on blog</p>"


@app.route('/blog/2020/dogs')
def blog2():
    return "<p>These are my dogs. a blog post about dogs</p>"


@app.route('/about.html')
def about():
    return render_template('./about.html')


