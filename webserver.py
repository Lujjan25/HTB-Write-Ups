from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if '..' in self.path:
            self.path = '/index.html'
        if self.path == '/':
            self.path = '/index.html'
        try:
            header = open('header.html').read()
            file_to_open = open(self.path[1:]).read().replace('<!--header-->', header)
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()
