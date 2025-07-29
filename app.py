from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

OLLAMA_API = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen:7b-chat"


@app.route("/")
def index():
    return render_template("index.html", model=OLLAMA_MODEL)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": user_input,
        "stream": False
    }
    response = requests.post(OLLAMA_API, json=payload)
    result = response.json()
    return jsonify({"response": result.get("response", "[Error] No response")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009)
