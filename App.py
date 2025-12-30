from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    return jsonify({"response": f"Tu mensaje fue: '{user_message}'"})

if __name__ == "__main__":
    app.run(debug=True)