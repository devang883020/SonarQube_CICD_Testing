from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def health():
    return jsonify(
        status="ok",
        message="MyApp is running successfully"
    ), 200


@app.route("/add/<int:a>/<int:b>", methods=["GET"])
def add(a: int, b: int):
    return jsonify(result=a + b), 200


@app.route("/subtract/<int:a>/<int:b>", methods=["GET"])
def subtract(a: int, b: int):
    return jsonify(result=a - b), 200


@app.route("/divide/<int:a>/<int:b>", methods=["GET"])
def divide(a: int, b: int):
    if b == 0:
        return jsonify(error="division by zero"), 400
    return jsonify(result=a / b), 200


if __name__ == "__main__":
    # VERY IMPORTANT for Kubernetes
    app.run(host="0.0.0.0", port=5000)
