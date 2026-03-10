import jwt

def decode_id_token(id_token):
    decoded_token = jwt.decode(
        id_token,
        options={"verify_signature": False}
    )

    return decoded_token