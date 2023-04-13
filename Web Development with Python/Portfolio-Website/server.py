from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'Form submitted hoooraaayyyy'