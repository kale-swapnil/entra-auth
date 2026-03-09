import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

SCOPES = os.getenv("SCOPES").split()

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

AUTHORIZATION_ENDPOINT = f"{AUTHORITY}/oauth2/v2.0/authorize"
TOKEN_ENDPOINT = f"{AUTHORITY}/oauth2/v2.0/token"

GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0"