#!/usr/bin/env python3
import http.server
import socketserver
import sys
import os
import json
from urllib.parse import urlparse, parse_qs
import urllib.request
import ssl

class OptionsAPIHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='/home/user/webapp', **kwargs)

    def do_GET(self):
        parsed_url = urlparse(self.path)
        
        # Handle API routes
        if parsed_url.path.startswith('/api/'):
            self.handle_api_request(parsed_url)
        else:
            # Serve static files
            super().do_GET()
    
    def handle_api_request(self, parsed_url):
        try:
            query_params = parse_qs(parsed_url.query)
            endpoint = parsed_url.path
            
            # Mock API responses for demo purposes
            if '/api/polygon' in endpoint:
                mock_data = {
                    "results": [{"c": 450.25, "p": 2.15}],
                    "status": "OK"
                }
            elif '/api/fmp' in endpoint:
                mock_data = [{"price": 450.25, "symbol": "SPY"}]
            else:
                mock_data = {"error": "Endpoint not found"}
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(mock_data).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def log_message(self, format, *args):
        sys.stdout.write(f"{self.log_date_time_string()} - {format%args}\n")
        sys.stdout.flush()

if __name__ == "__main__":
    PORT = 3000
    with socketserver.TCPServer(("0.0.0.0", PORT), OptionsAPIHandler) as httpd:
        print(f"Server running on port {PORT}")
        sys.stdout.flush()
        httpd.serve_forever()