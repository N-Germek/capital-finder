from http.server import BaseHTTPRequestHandler
import requests

class Handler(BaseHTTPRequestHandler):

    r = requests.get('https://restcountries.com/v3.1/capital/lima', data= {'': ''},auth=('user', 'pass'))
    r.status_code
    200
    r.headers['content-type']
    'application/json; charset=utf8'
    r.encoding
    'utf-8'
    r.text
    '{"type":"User"...'
    r.json()
    {'private_gists': 419, 'total_private_repos': 77, ...}