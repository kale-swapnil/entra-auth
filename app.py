from flask import Flask, session, redirect, url_for, request, render_template
from config import CLIENT_ID
from auth_routes import auth_bp

app = Flask(__name__)

app.secret_key= "super-secret-session-key"
app.register_blueprint(auth_bp)

@app.route("/")
def home():
    return render_template ("index.html")


@app.route("/tokens")
def tokens():
    return "Token view not implemented yet"

@app.route("/logout")
def logout():
    return "Logout not implemented yet"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)   