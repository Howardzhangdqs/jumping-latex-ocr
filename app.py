from main import main
import cv2
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return open("index.html", encoding="utf-8").read()


@app.route("/api/ocr", methods=["POST"])
def ocr():
    print("/api/ocr", request.files)

    img = request.files["file"]
    img = cv2.imdecode(np.frombuffer(img.read(), np.uint8), cv2.IMREAD_COLOR)

    tex = main(img)

    return jsonify({"tex": tex})


if __name__ == "__main__":
    app.run(debug=False, port=5000)
