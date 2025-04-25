from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from hanspell import spell_checker

app = Flask(__name__)

# CORS 설정: 모든 경로, 모든 origin 허용
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route('/check', methods=['POST', 'OPTIONS'])
def check():
    if request.method == 'OPTIONS':
        # Preflight 요청 직접 응답
        response = make_response('', 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    # POST 요청 처리
    data = request.get_json()
    text = data.get("text", "")
    res = spell_checker.check(text)
    response = jsonify({"result": res.checked})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
