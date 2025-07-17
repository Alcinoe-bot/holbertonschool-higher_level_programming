#!/usr/bin/python3
from flask import Flask, render_template, request
import json, csv, os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    with open(json_path, 'r') as file:
        data = json.load(file)
    return render_template('items.html', items=data["items"])

def read_json_data():
    with open('products.json') as f:
        return json.load(f)["products"]

def read_csv_data():
    with open("products.csv", newline='') as f:
        return list(csv.DictReader(f))

@app.route('/products')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id')

    if source == "json":
        products = read_json_data()
    elif source == "csv":
        products = read_csv_data()
    else:
        return render_template("product_display.html", error="Wrong source")

    if prod_id:
        filtered = [p for p in products if str(p.get("id")) == prod_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found")
        return render_template("product_display.html", products=filtered)

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
