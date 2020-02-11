from flask import Flask
from benchmark_book import book_list
import json

app = Flask("book-sorting")

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/jquery-3.4.1.min.js")
def jquery():
    return app.send_static_file("jquery-3.4.1.min.js")

@app.route("/data")
def data():
    return json.dumps([book.__dict__ for book in book_list])