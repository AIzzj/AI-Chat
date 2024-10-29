from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze_emotion', methods=['POST'])
def analyze_emotion():
    # 处理请求的逻辑
    return jsonify({'emotion': 'happy'}) 