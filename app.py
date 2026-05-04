from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    print("Flask App runs in normal mode")
    return 'Hello, Docker CI/CD! from Timokhin V.M.'

@app.route("/api/sum/<int:a>/<int:b>")
def get_sum(a, b):
    return jsonify({"result": a + b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
