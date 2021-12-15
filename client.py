from typing import Any, Dict
import requests
import os

from bs4 import BeautifulSoup
from requests.models import Response
import json

BASE_URL = "https://forecastercalculator.integral.co.nz"


def get_cookies():
    if not os.path.exists('.cookies'):
        return dict[str, str]()

    with open('.cookies') as f:
        cookies = dict(x.split('=') for x in f.readlines())
        return cookies


def save_cookies(cookies: Dict[str, str]):
    with open('.cookies', 'w') as f:
        for key, value in cookies.items():
            f.write(f'{key}={value}\n')


class ApiClient:
    def __init__(self, username: str, password: str) -> None:
        self.http = requests.session()
        self.username = username
        self.password = password
        # self.http.cookies.update(get_cookies())

    def make_request(self, path: str, method: str, body=None) -> Response:
        url = f'{BASE_URL}{path}'
        return self.http.request(method=method, url=url, data=body)

    def forge_post(self, path: str, body: dict[str, Any]) -> Response:
        get_request = self.make_request(path, 'GET')
        html = BeautifulSoup(get_request.text)
        token = html.find('input', {'name': '__RequestVerificationToken'})
        body['__RequestVerificationToken'] = token.attrs['value']
        return self.make_request(path, method='POST', body=body)

    def ensure_loggedin(self):
        if len(self.http.cookies) != 0:
            return

        login_response = self.forge_post('/Account/Login', body={
            'Email': self.username,
            'Password': self.password,
            'RememberMe': True
        })

        save_cookies(self.http.cookies.get_dict())

    def simulate(self, lat: float, lng: float, commands: list, altitude: float = 300, site_index: float = 30, index_300: float = 26, index_500: float = 18.4):
        json_data = {
            'site': {
                'latitude': lat,
                'longitude': lng,
                'altitude': altitude,
                'siteIndex': site_index,
                'the300Index': index_300,
                'the500Index': index_500
            },
            'regime': {
                'commands': commands
            },
            "results": {
                "outputFiles": [],
                "status": {
                    "failure": False
                }
            }
        }

        json_str = json.dumps(json_data)
        response = self.make_request('/Simulate/DoSimulation', 'POST', {'simulateViewModelJSON': json_str })
        return response
