# this is implementing for the server in Vercel
from http.server import BaseHTTPRequestHandler
# this is importing from datetime library the date and time
from datetime import datetime


class Handler(BaseHTTPRequestHandler):

    # this will access the built-in method in the HTTP file
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # datetime: get the date and time now, .strftime: returns string representing date formatted as year, month,
        # day, hour, minute, second,.encode:
        self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
        return
