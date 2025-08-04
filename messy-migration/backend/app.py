from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import jwt
import datetime
from functools import wraps
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
app = Flask(__name__)
CORS(app)

DB_PATH = 'users.db'
SECRET_KEY = os.getenv('SECRET_KEY')
print("Loaded SECRET_KEY:", SECRET_KEY)


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Token is missing"}), 401
        try:
            token = token.replace("Bearer ", "")
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/home')
def home():
    return jsonify({"message": "User Management System is running"}), 200

@app.route('/users', methods=['GET'])
@token_required
def get_all_users():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return jsonify([dict(user) for user in users]), 200

@app.route('/user/<int:user_id>', methods=['GET'])
@token_required
def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    if user:
        return jsonify(dict(user)), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
@token_required
def create_user():
    data = request.get_json()
    print(data)
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    gender = data.get('gender')

    print(name, email, password,gender)
    if not all([name, email, password, gender]):
        return jsonify({"error": "Missing fields"}), 400
    
    print(name, email, password,gender)
    conn = get_db_connection()
    conn.execute("INSERT INTO users (name, email, gender, password) VALUES (?, ?, ?, ?)", (name, email, gender, password))
    conn.commit()
    conn.close()
    return jsonify({"message": "User created"}), 201

@app.route('/user/<int:user_id>', methods=['PUT'])
@token_required
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    gender = data.get('gender')
    print(name,email,gender,user_id)

    if not all([name, email,gender]):
        return jsonify({"error": "Missing fields"}), 400

    conn = get_db_connection()
    conn.execute("UPDATE users SET name = ?, email = ? , gender=? WHERE id = ?", (name, email, gender,user_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "User updated"}), 200

@app.route('/user/<int:user_id>', methods=['DELETE'])
@token_required
def delete_user(user_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": f"User {user_id} deleted"}), 200

@app.route('/search', methods=['GET'])
@token_required
def search_users():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Please provide a name to search"}), 400

    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users WHERE name LIKE ?", (f"%{name}%",)).fetchall()
    conn.close()
    return jsonify([dict(user) for user in users]), 200

@app.route('/', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password)).fetchone()
    conn.close()

    if user:
        token = jwt.encode({
            'user_id': user['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }, SECRET_KEY, algorithm="HS256")
        return jsonify({"status": "success", "token": token}), 200
    return jsonify({"status": "failed"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)
