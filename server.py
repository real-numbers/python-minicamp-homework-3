from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('food.html')

@app.route('/addfood', methods = ['POST'])
def addfood():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    name = request.form['name']
    calories = request.form['calories']
    cuisine = request.form['cuisine']
    is_vegetarian = request.form['is_vegetarian']
    is_gluten_free = request.form['is_gluten_free']

    try:
        cursor.execute('INSERT INTO foods(name,calories,cuisine,is_vegetarian,is_gluten_free) VALUES(?,?,?,?,?)',(name,calories,cuisine,is_vegetarian,is_gluten_free))
        conn.commit()
        message = "success"

    except:
        conn.rollback()
        message = "fail"

    finally:
        conn.close()
        return render_template('result.html')

@app.route('/foodlist')
def foodlist():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM foods')
    foodlist = cursor.fetchall()
    conn.close()
    return jsonify(foodlist)
