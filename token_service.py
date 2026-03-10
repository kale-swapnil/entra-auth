

from urllib import response

import requests 
from config import CLIENT_SECRET, SCOPES, TOKEN_ENDPOINT, REDIRECT_URI, CLIENT_ID


def exchange_code_for_token(auth_code):
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
        "scope": " ".join(SCOPES)
    }

    response = requests.post(
        TOKEN_ENDPOINT,
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )


    return response.json()


def refresh_access_token(refresh_token):
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "scope": " ".join(SCOPES)
    }

    response = requests.post(
        TOKEN_ENDPOINT,
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    return response.json()