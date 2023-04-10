from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    return render_template('./index.html')


@app.route('/about.html')
def about():
    return render_template('./about.html')


@app.route('/components.html')
def components():
    return render_template('./components.html')


@app.route('/thankyou.html')
def thankyou():
    return render_template('./thankyou.html')


@app.route('/work.html')
def work():
    return render_template('./work.html')


@app.route('/works.html')
def works():
    return render_template('./works.html')


@app.route('/contact.html')
def contact():
    return render_template('./contact.html')