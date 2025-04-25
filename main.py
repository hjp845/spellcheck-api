from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from hanspell import spell_checker

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 이건 자동 적용 목적

@app.route('/check', methods=['POST', 'OPTIONS'])
def check():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    data = request.get_json()
    text = data.get("text", "")
    res = spell_checker.check(text)

    # ✅ POST 응답에도 강제로 헤더 삽입
    response = jsonify({"result": res.checked})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
