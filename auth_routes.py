
from flask import Blueprint, redirect, request, session
import urllib.parse
import uuid

from config import AUTHORIZATION_ENDPOINT, CLIENT_ID, REDIRECT_URI, SCOPES
from jwt_decoder import decode_id_token
from token_service import exchange_code_for_token, refresh_access_token
from graph_service import get_user_profile
from token_store import token_store

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
    
    session.pop("oauth_state", None)
    
    if not auth_code:
        return "Authorization code missing", 400
    
    # session["auth_code"] = auth_code

    token_response = exchange_code_for_token(auth_code)

    if not token_response:
        return "Token exchange failed"
    
    user_session_id = str(uuid.uuid4())

    token_store[user_session_id] = {
        "access_token": token_response.get("access_token"),
        "id_token": token_response.get("id_token"),
        "refresh_token": token_response.get("refresh_token")
    }

    session["user_session_id"] = user_session_id
    
    return redirect("/profile")
    


@auth_bp.route("/profile")
def profile():


    user_session_id = session.get("user_session_id")

    if not user_session_id:
        return "User not authenticated"
    
    tokens = token_store.get(user_session_id)

    access_token = tokens.get("access_token")

   # if not access_token:
   #     return "User not authenticated"
    
    user_profile = get_user_profile(access_token)

    if "error" in user_profile:
        refresh_token = tokens.get("refresh_token")

        if not refresh_token:
            return "Refresh token missing"
        
        new_tokens = refresh_access_token(refresh_token)

        access_token = new_tokens.get("access_token")
        refresh_token = new_tokens.get("refresh_token")

        user_profile = get_user_profile("access_token")

    return user_profile