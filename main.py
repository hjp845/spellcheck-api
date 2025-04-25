from flask import Flask, request, jsonify
from flask_cors import CORS
from hanspell import spell_checker

app = Flask(__name__)

# ✅ 모든 라우트에 대해 모든 Origin 허용 + Preflight 지원
CORS(app, resources={r"/check": {"origins": "*"}}, supports_credentials=True)

@app.route('/check', methods=['POST', 'OPTIONS'])
def check():
    if request.method == 'OPTIONS':
        # ✅ Preflight 요청에 대한 CORS 응답 강제 추가
        response = app.make_response('', 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    data = request.get_json()
    text = data.get("text", "")
    res = spell_checker.check(text)
    return jsonify({"result": res.checked})
