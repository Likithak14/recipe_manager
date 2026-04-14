import http.server
import socketserver
import webbrowser
import os

# Always serve from the directory where THIS script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000
handler = http.server.SimpleHTTPRequestHandler

print(f"Serving at: http://localhost:{PORT}/index.html")

webbrowser.open(f"http://localhost:{PORT}/index.html")

with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()
