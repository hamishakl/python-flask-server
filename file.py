import http.server
import socketserver

PORT = 7000

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("Hello banana man")
httpd.serve_forever()
