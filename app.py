from flask import Flask, session, redirect, url_for, request
from config import CLIENT_ID

app = Flask(__name__)

app.secret_key= "super-secret-session-key"

@app.route("/")
def home():
    return "Oauth Home"

@app.route("/login")
def login():
    return "Login endpoint not implemented yet"


@app.route("/callback")
def callback():
    return "Callback not implemented yet"

@app.route("/tokens")
def tokens():
    return "Token view not implemented yet"

@app.route("/profile")
def profile():
    return "Profile not implemented yet"

@app.route("/logout")
def logout():
    return "Logout not implemented yet"

if __name__ == "__main__":
    app.run(debug=true)   