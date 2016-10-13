#!/usr/bin/env python
 
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
 
class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        request_path = self.path
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write("hello world!!")
        
    do_POST = do_GET    
    do_PUT = do_GET
    do_DELETE = do_GET
        
def main():
    port = 80
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()
 
        
if __name__ == "__main__":
    main()
