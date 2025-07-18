#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_data():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv_data():
    with open('products.csv', 'r', newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)


def read_sql_data(product_id=None):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    if product_id:
        cursor.execute('SELECT id, name, category, price FROM Products WHERE id = ?', (product_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return [{
                'id': str(row[0]),
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }]
        else:
            return None
    else:
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        products = []
        for row in rows:
            products.append({
                'id': str(row[0]),
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error='Wrong source')

    try:
        if source == 'json':
            products = read_json_data()
            if product_id:
                products = [p for p in products if str(p.get('id')) == product_id]
                if not products:
                    return render_template('product_display.html', error='Product not found')

        elif source == 'csv':
            products = read_csv_data()
            if product_id:
                products = [p for p in products if str(p.get('id')) == product_id]
                if not products:
                    return render_template('product_display.html', error='Product not found')

        elif source == 'sql':
            products = read_sql_data(product_id)
            if products is None:
                return render_template('product_display.html', error='Product not found')

    except FileNotFoundError:
        return render_template('product_display.html', error='File not found')
    except sqlite3.Error:
        return render_template('product_display.html', error='Database error')

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
