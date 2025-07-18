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

            if product_id:
                products = [p for p in products if str(p.get('id')) == product_id]
                if not products:
                    return render_template('product_display.html', error='Product not found')

        elif source == 'csv':
            with open('products.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                products = list(reader)

            if product_id:
                products = [p for p in products if str(p.get('id')) == product_id]
                if not products:
                    return render_template('product_display.html', error='Product not found')

        elif source == 'sql':
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            if product_id:
                cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
                row = cursor.fetchone()
                if row:
                    products = [row]
                else:
                    return render_template('product_display.html', error='Product not found')
            else:
                cursor.execute('SELECT * FROM Products')
                products = cursor.fetchall()

            conn.close()

    except FileNotFoundError:
        return render_template('product_display.html', error='File not found')
    except sqlite3.Error:
        return render_template('product_display.html', error='Database error')

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
