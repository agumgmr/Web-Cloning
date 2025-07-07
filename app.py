# app.py
from flask import Flask, render_template, request
import requests
from databases import sql

db = sql().read_data()

app = Flask(__name__)

@app.route('/')
def index():
    database = db
    return render_template('index.html', database=db)

@app.route('/details/<id>')
def details(id):
    details_url = id
    details = sql().select_data(id)
    details0 = details[0]
    return render_template('details.html', details=details0)

if __name__ == "__main__":
    app.run(debug=True)
