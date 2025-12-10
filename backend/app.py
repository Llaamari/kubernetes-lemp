from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "appdb")
    )

@app.route("/api/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/api/init-db")
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)
    cursor.execute("""
        INSERT INTO users (name, email)
        VALUES ('John Doe', 'john@example.com'),
               ('Jane Smith', 'jane@example.com')
    """)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Database initialized"})

@app.route("/api/users")
def users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route("/api/add-user", methods=["POST"])
def add_user():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (name, email)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "User added"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
