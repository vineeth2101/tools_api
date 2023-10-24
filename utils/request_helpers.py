import requests
from requests.adapters import HTTPAdapter

def make_request(
    method: str,
    endpoint: str,
    params: dict = None,
    token: str = None,
    headers: dict = None,
    body: object = None,
    cookies: dict = None,
) -> object:
    """Base Function for all requests"""
    if headers is None:
        headers = {"Authorization": f"SRRA_Token {token}"}
    else:
        headers.update({"Authorization": f"SRRA_TOKEN {token}"})
    session = requests.Session()
    adapter = HTTPAdapter()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    res = session.request(
        method, endpoint, params=params, headers=headers, json=body, cookies=cookies
    )
    return res