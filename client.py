from typing import Any, Dict
import requests
import os

from bs4 import BeautifulSoup
from requests.models import Response
import json
import urllib
import urllib3

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

    def make_request(self, path: str, method: str, body=None, headers=None) -> Response:
        url = f'{BASE_URL}{path}'
        return self.http.request(method=method, url=url, data=body, headers=headers)

    def forge_post(self, path: str, body: dict[str, Any]) -> Response:
        get_request = self.make_request(path, 'GET')
        html = BeautifulSoup(get_request.text, features='lxml')
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
        json_data = {"site": {"latitude": 38.221, "longitude": 176.07, "altitude": 660, "siteIndex": 30, "the300Index": 26, "the500Index": 18.4}, "regime": {"commands": [{"condition": "Date+=+[Jun+2000]", "event": {"$type": "Scion.ForecasterCalculator.Models.PlantEventViewModel,+Scion.ForecasterCalculator", "species": "PSMEN", "plantStocking": 1650}}, {"condition": "Date+=+[Jun+2010]", "event": {"$type": "Scion.ForecasterCalculator.Models.MeasurementEventViewModel,+Scion.ForecasterCalculator", "stocking": 1500, "basalArea": 6.8, "meanTopHeight": 5.9}}, {"condition": "Crop.Age+=+15", "event": {"$type": "Scion.ForecasterCalculator.Models.ThinEventViewModel,+Scion.ForecasterCalculator", "residualStocking": 750}}, {
            "condition": "Crop.Age+=+40", "event": {"$type": "Scion.ForecasterCalculator.Models.ClearfellEventViewModel,+Scion.ForecasterCalculator", "pricedLogProductDefinitions": [{"name": "DS", "description": "Sawlog", "pricePerM3": 160, "maxCut": 99, "priority": 1}, {"name": "CF+", "description": "", "pricePerM3": 110, "maxCut": 99, "priority": 2}, {"name": "CF-", "description": "", "pricePerM3": 90, "maxCut": 99, "priority": 3}, {"name": "Pulp", "description": "Pulp+log", "pricePerM3": 40, "maxCut": 99, "priority": 4}], "cuttingStrategyName": "Douglas-fir", "cuttingStrategyDescription": "", "specie": "PSMEN", "cutCost": 1, "buckingMode": "MaximumValue"}}]}, "results": {"outputFiles": [], "status": {"failure": False}}}

        json_str = json.dumps(json_data, separators=(',',':'))
        body = urllib.parse.urlencode({
            'simulateViewModelJSON': json_str
        }, safe=':+')
        response = self.make_request(
            '/Simulate/DoSimulation', 'POST', body,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'accept': 'application/json, text/javascript, */*; q=0.01'
            })
        return response
