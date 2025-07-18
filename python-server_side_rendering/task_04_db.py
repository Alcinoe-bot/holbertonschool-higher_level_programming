#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error='Wrong source')

    try:
        if source == 'json':
            with open('products.json', 'r') as file:
                products = json.load(file)

        elif source == 'csv':
            with open('products.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                products = list(reader)

        elif source == 'sql':
            products = read_sql_data()

    except FileNotFoundError:
        return render_template('product_display.html', error='File not found')
    except sqlite3.Error:
        return render_template('product_display.html', error='Database error')

    if product_id:
        products = [p for p in products if str(p.get('id')) == str(product_id)]
        if not products:
            return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=products)


def read_sql_data():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return products

if __name__ == '__main__':
    app.run(debug=True, port=5000)
