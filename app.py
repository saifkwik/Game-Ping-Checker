import main

# FLASK
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/gamepings', methods=['GET'])
def stuff():
    result = main.display(main.dns_in_db)
    return result


@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html', data=stuff())
