from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="my_database",
    user="my_user",
    password="my_password",
    host="localhost",  # 또는 클라우드 호스트 주소
    port="5432"
)

@app.route('/')
def home():
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    cur.close()
    return jsonify({"PostgreSQL Version": version[0]})

if __name__ == '__main__':
    app.run(debug=True)

# localhost
# 5432