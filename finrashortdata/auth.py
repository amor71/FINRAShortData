"""Implement FINRA API authentication"""
import requests
from requests.auth import HTTPBasicAuth

url = "https://ews.fip.finra.org/fip/rest/ews/oauth2/access_token"
params = {"grant_type": "client_credentials"}


def auth(client_id: str, secret: str) -> str:
    """Generate FINRA API Token based on api client id and secret.

    Token has expiration duration, and may need to be refreshed.

    Input Arguments: client_id, secret FINRA API credentials, per environment (test or prod).
    Returns: If successful returns generated token, otherwise throws exception.
    """
    if not client_id or not secret:
        raise TypeError("client_id and secret can not be None")

    auth = HTTPBasicAuth(client_id, secret)
    r = requests.post(url=url, params=params, auth=auth)
    r.raise_for_status()

    return r.json()["access_token"]
