# from http.server import BaseHTTPRequestHandler
# import requests
#
#
# class Handler(BaseHTTPRequestHandler):
#
#     def do_GET(self):
#
#     need to find out if able to complete a requests.get for country and capital at same time?
#     also how do you properly inpout search parameters in url for python?
#         r = requests.get('https://restcountries.com/v3.1/name/{name}/capital-finder?country=Chile',
#                          'https://restcountries.com/v3.1/capital/{capital}/capital-finder?capital=Santiago', auth=('user', 'pass'))
#         r.send_response(200)
#         r.send_headers('Content-type', 'text/plain')
#         r.end_headers()
#     need to properly target index x and y variables for message to be complete.
#         message = "The capital of X is Y"
#         r.wfile.write(str().encode(message.encode))
#         return
