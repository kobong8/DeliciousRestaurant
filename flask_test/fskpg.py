from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="dbname",
    user="user",
    password="password",
    host="host",
    port="5432"
)

@app.route('/')
def home():
    # return "Hello, World!"
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    cur.close()
    return jsonify({"PostgreSQL Version": version[0]})

if __name__ == '__main__':
    app.run(host="host", port=5432)
    # app.run(debug=True)

#  * Serving Flask app 'fskpg'
#  * Debug mode: off
# 액세스 권한에 의해 숨겨진 소켓에 액세스를 시도했습니다
#
# Process finished with exit code 1
