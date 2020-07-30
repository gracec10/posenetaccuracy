import http.server
import json

FILE = 'posenet.html'
PORT = 8000

class TestHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        print(self.headers)
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        new_data = json.loads(self.data_string.decode('utf-8'))

        with open('posenet.json') as f:
            data = json.load(f)

        data.append(new_data)

        with open('posenet.json', 'w') as f:
            json.dump(data, f)

        self.flush_headers()

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = http.server.HTTPServer(server_address, TestHandler)
    server.serve_forever()

start_server()