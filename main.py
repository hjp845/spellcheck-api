from flask import Flask, request, jsonify
from flask_cors import CORS
from hanspell import spell_checker

app = Flask(__name__)
CORS(app)  # CORS 허용 설정

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    text = data.get("text", "")
    res = spell_checker.check(text)
    return jsonify({"result": res.checked})
