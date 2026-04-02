import http.server, socketserver

PORT = 8080
DIRECTORY = "/Users/carolynscanlon/Desktop/Prisms Coaching Project"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass  # suppress request logs

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
