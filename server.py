from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import time
from ml.classifier import final_classify

hostName = "localhost"
hostPort = 9000

class ANNServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        query_components = parse_qs(urlparse(self.path).query)
        if "sentence" in query_components:
            sentence = query_components["sentence"] 
            result = final_classify(sentence[0])
            result = '{"result":'+ result + '}'
            self.wfile.write(bytes("%s" % result, "utf-8"))

annServer = HTTPServer((hostName, hostPort), ANNServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    annServer.serve_forever()
except KeyboardInterrupt:
    pass

annServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))