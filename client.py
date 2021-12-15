from typing import Dict
import requests
import os

from requests.models import Response
from requests.sessions import session

BASE_URL = "https://forecastercalculator.integral.co.nz"

def get_cookies():
    if not os.path.exists('.cookies'):
        return dict[str, str]()
    
    with open('.cookies') as f:
        cookies = dict(x.split('=') for x in f.readlines())
        return cookies

def save_cookies(cookies: Dict[str,str]):
    with open('.cookies', 'w') as f:
        for key, value in enumerate(cookies):
            f.write(f'{key}={value}\n')

class ApiClient:
    def __init__(self, username: str, password: str) -> None:
        self.http = requests.session()
        self.username = username
        self.password = password
        self.http.cookies.update(get_cookies())

    def make_request(self, path: str, method: str, body=None) -> Response:
        url = f'{BASE_URL}{path}'
        return self.http.request(method=method, url=url, data=body)

    def ensure_loggedin(self):
        if len(self.http.cookies) != 0:
            return

        response = self.make_request('/Account/Login', 'POST', body={
            'Email': self.username,
            'Password': self.password,
            'RememberMe': True
        })

        save_cookies(self.http.cookies.get_dict())

        
