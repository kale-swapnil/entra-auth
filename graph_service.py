

import requests

from config import GRAPH_API_ENDPOINT


def get_user_profile(access_token):
    endpoint = f"{GRAPH_API_ENDPOINT}/me"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(endpoint, headers=headers)

    return response.json()