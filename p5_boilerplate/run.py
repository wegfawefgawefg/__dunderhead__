from http.server import HTTPServer, SimpleHTTPRequestHandler

def start_server(bind="127.0.0.1", port=4400):
    print(f'Starting a development server at http://{bind}:{port}')
    httpd = HTTPServer((bind, int(port)), SimpleHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    start_server()
