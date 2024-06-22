from main import main
from flask import Flask, request, jsonify
import cv2
import numpy as np


# 创建服务器
# / 返回 index.html
# /api/ocr 返回识别结果

app = Flask(__name__)


@app.route("/")
def index():
    return open("index.html", encoding="utf-8").read()


@app.route("/api/ocr", methods=["POST"])
def ocr():
    print("/api/ocr", request.files)
    img = request.files["file"]
    
    # 将img转为cv2.Mat
    img = cv2.imdecode(np.frombuffer(img.read(), np.uint8), cv2.IMREAD_COLOR)

    # 识别
    tex = main(img)
    print(tex)
    
    return jsonify({"tex": tex})



if __name__ == "__main__":
    app.run(port=5000)
