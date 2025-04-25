from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from hanspell import spell_checker

app = Flask(__name__)
CORS(app, resources={r"/check": {"origins": "*"}}, supports_credentials=True)

@app.route('/check', methods=['POST', 'OPTIONS'])
def check():
    if request.method == 'OPTIONS':
        response = make_response('', 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    try:
        data = request.get_json(force=True)
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400

        res = spell_checker.check(text)

        if not hasattr(res, "checked"):
            return jsonify({"error": "Spellcheck failed. Please try again later."}), 500

        response = jsonify({"result": res.checked})
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    except Exception as e:
        print(f"서버 에러: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
