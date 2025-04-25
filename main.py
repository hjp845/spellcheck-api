from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from hanspell import spell_checker

app = Flask(__name__)

# 💡 모든 경로에 대해 모든 Origin 허용
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route('/check', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*')  # 💥 명시적으로 CORS 허용 (Flask-CORS용 데코레이터)
def check():
    if request.method == 'OPTIONS':
        return '', 200  # Preflight 요청에 200 응답

    data = request.json
    text = data.get("text", "")
    res = spell_checker.check(text)
    return jsonify({"result": res.checked})
