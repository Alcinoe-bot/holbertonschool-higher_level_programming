#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

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
    with open('items.json', 'r') as file:
        items = json.load(file).get('items')
    return render_template('items.html', items=items)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error='Wrong source')

    try:
        if source == 'json':
            with open('products.json', 'r') as file:
                products = json.load(file)
        else:  # source == 'csv'
            with open('products.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                products = list(reader)
    except FileNotFoundError:
        return render_template('product_display.html', error='File not found')

    if product_id:
        filtered = [p for p in products if str(p.get('id')) == str(product_id)]
        if not filtered:
            return render_template('product_display.html', error='Product not found')
        products = filtered

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
