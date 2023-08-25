from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os


app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(base_dir, 'planets.db')}"


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/home')
def home():
    return 'This is my home'


@app.route('/not_found')
def not_found():
    return jsonify(message='that resource was not found'), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message=f'Sorry {name} you are not old enough'), 401
    else:
        return jsonify(message=f' Welcome {name}, you are old enough')


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message=f'Sorry {name} you are not old enough'), 401
    else:
        return jsonify(message=f' Welcome {name}, you are old enough')


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the Planetary API.')


if __name__ == '__main__':
    app.run()
