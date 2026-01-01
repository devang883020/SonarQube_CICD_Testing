from flask import Flask, jsonify, request
from logic import add, subtract, divide

app = Flask(__name__)

@app.route("/add")
def add_route():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify(result=add(a, b)), 200

@app.route("/subtract")
def subtract_route():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify(result=subtract(a, b)), 200

@app.route("/divide")
def divide_route():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    try:
        return jsonify(result=divide(a, b)), 200
    except ValueError as e:
        return jsonify(error=str(e)), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
