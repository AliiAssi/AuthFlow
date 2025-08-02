from flask import Flask, render_template, request, jsonify
from google.oauth2 import id_token
from google.auth.transport import requests as grequests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Get Google Client ID from environment variable
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')

@app.route("/")
def login_page():
    return render_template("login.html", client_id=GOOGLE_CLIENT_ID)

@app.route("/google-login", methods=["POST"])
def google_login():
    token = request.json.get("token")
    try:
        idinfo = id_token.verify_oauth2_token(token, grequests.Request(), GOOGLE_CLIENT_ID)
        user_email = idinfo.get("email")
        name = idinfo.get("name")
        print(f"User email: {user_email}, Name: {name}")
        return jsonify({
            "status": "success",
            "email": user_email,
            "name": name
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)