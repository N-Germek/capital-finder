from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        BASE_URL = "https://restcountries.com/v3.1"
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        country = dic.get("country")
        capital = dic.get("capital")

        if country and capital:
            message = "Located country and capital"
        elif country:
            url = f"{BASE_URL}/name/{country}"
            req = requests.get(url)
            info = req.json()
            capitals = info[0]["capital"]
            joined_caps = " and ".join(capitals)
            message = f"The capital of {country} is {joined_caps}"
        elif capital:
            url = f"{BASE_URL}/capital/{capital}"
            req = requests.get(url)
            info = req.json()
            message = str(info)

        else:
            message = "Supply a country or capital please"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())

        return
