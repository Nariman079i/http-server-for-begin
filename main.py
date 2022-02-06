from http.server import HTTPServer, CGIHTTPRequestHandler

adr = ("",8000)
httpd = HTTPServer(adr , CGIHTTPRequestHandler)

httpd.serve_forever()