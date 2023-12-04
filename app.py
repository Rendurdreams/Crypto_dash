from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    conn = mysql.connector.connect(user='rendur', password='newpassword', host='db', database='mydatabase')
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM cryptocurrencies")
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)