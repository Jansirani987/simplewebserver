from http.server import HTTPServer, BaseHTTPRequestHandler
content="""
html>
    <body>
        <h1 align="center"> Jansi rani 24900239</h1>
        <ol type="I">
            <li>Device name	Jansi-AA </li>
            <li>
                Processor	Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz   2.50 GHz
                </li>
            <li>Installed RAM	16.0 GB (15.9 GB usable)
                </li>
            <li>Device ID	DC34E5DC-17B2-45BB-8D02-7E5E4ED9B423
                </li>
            <li>Product ID	00342-50603-63490-AAOEM
                </li>
            <li>System type	64-bit operating system, x64-based processor
                </li>
            <li>Pen and touch	No pen or touch input is available for this display
                </li>
        </ol>

    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()