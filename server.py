import http.server
import socketserver
import os
import sys

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PORT = 80

class AtlantisPlayerHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(DIRECTORY)
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), AtlantisPlayerHandler) as httpd:
            print(f"TYSON Atlantis Standalone Player running on http://localhost:{PORT} (Directory: {DIRECTORY})")
            sys.stdout.flush()
            httpd.serve_forever()
    except (PermissionError, OSError) as e:
        PORT = 8080
        with socketserver.TCPServer(("", PORT), AtlantisPlayerHandler) as httpd:
            print(f"TYSON Atlantis Standalone Player running on http://localhost:{PORT} (Directory: {DIRECTORY})")
            sys.stdout.flush()
            httpd.serve_forever()
