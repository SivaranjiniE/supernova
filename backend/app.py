from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# ------------------ DATABASE SETUP ------------------

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    # Votes table
    c.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            option TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()

# ------------------ SIGNUP ------------------

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    password = data['password']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return jsonify({"message": "User created successfully"})
    except:
        return jsonify({"message": "User already exists"})

# ------------------ LOGIN ------------------

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    if user:
        return jsonify({"message": "Login successful", "user_id": user[0]})
    else:
        return jsonify({"message": "Invalid credentials"})

# ------------------ VOTE ------------------

@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    user_id = data['user_id']
    option = data['option']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    try:
        c.execute("INSERT INTO votes (user_id, option) VALUES (?, ?)", (user_id, option))
        conn.commit()
        return jsonify({"message": "Vote submitted"})
    except:
        return jsonify({"message": "You have already voted"})

# ------------------ RESULTS ------------------

@app.route('/results', methods=['GET'])
def results():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT option, COUNT(*) FROM votes GROUP BY option")
    data = c.fetchall()

    result = []
    for row in data:
        result.append({
            "option": row[0],
            "votes": row[1]
        })

    winner = None
    if data:
        winner = max(data, key=lambda x: x[1])[0]

    return jsonify({
        "results": result,
        "winner": winner
    })

# ------------------ RUN ------------------

@app.route('/')
def home():
    return "Backend is running!"

if __name__ == '__main__':
    app.run(debug=True)