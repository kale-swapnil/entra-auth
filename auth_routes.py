from flask import Blueprint, redirect, request, session
import urllib
import uuid

from config import AUTHORIZATION_ENDPOINT, CLIENT_ID, REDIRECT_URI, SCOPES
from jwt_decoder import decode_id_token
from token_service import exchange_code_for_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login")
def login():
    
    state = str(uuid.uuid4())

    session["oauth_state"] = state

    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "response_mode": "query",
        "scope": " ".join(SCOPES),
        "state": state

    }

    authorization_url = AUTHORIZATION_ENDPOINT + "?" + urllib.parse.urlencode(params)

    return redirect(authorization_url)

@auth_bp.route("/callback")
def callback():
    auth_code = request.args.get("code")
    returned_state = request.args.get("state")

    expected_state = session.get("oauth_state")

    if not returned_state or returned_state != expected_state:
        return "State Validation failed", 400
    
    if not auth_code:
        return "Authorization code missing", 400
    
   # session["auth_code"] = auth_code

    token_response = exchange_code_for_token(auth_code)

    #if not token_response:
    #    return "Token exchange failed"
    
    #print(token_response)


    session["access_token"] = token_response.get("access_token")
    session["id_token"] = token_response.get("id_token")
    session["refresh_token"] = token_response.get("refresh_token")

    decoded_token = decode_id_token(session["id_token"])

    return decoded_token
   # return f"Authorization code received: {auth_code}"

   # return f"Token response received: {token_response}"

   # return token_response