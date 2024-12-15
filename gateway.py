import json, socketserver, http.server, requests

#default port for pythons http.server
PORT = 8000

# 3 storage services, one, two, and three. where 0 is encountered returned not found
# two functions: check status and get data (with eg. round robyn or straight up random?)

#list of storages
storages = ["http://storage1:5000", "http://storage2:5000", "http://storage3:5000"]

class Gateway(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):

        #debugging print
        print(f"Requested path: {self.path}")

        if self.path == "/status" or self.path.rstrip("/") == "/status":
            # empty status report
            status_report = {}
            for s in storages:
                try:
                    # two second timeout should be enough for local network
                    response = requests.get(f"{s}/status", timeout=2)
                    status_report[s] = response.json()["status"]
                except requests.exceptions.RequestException:
                    status_report[s] = "down"
            self.send_response(200)
            print(json.dumps(status_report))

        elif self.path == "/data" or self.path.rstrip("/") == "/data":
            for s in storages:
                try:
                    response = requests.get(f"{s}/data", timeout=2)
                    if response.status_code == 200:
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(response.content)
                        print(response.json())
                        return
                except requests.exceptions.RequestException:
                    continue
        else:
            self.send_response(404)
            print("404 Not Found")

if __name__ == '__main__':
    # TCPServer constructor("empty tuple that listens to all interfaces, PORT number")
    with socketserver.TCPServer(("", PORT), Gateway) as httpd:
        # this should be port 8000
        print(f"Running on port ", {PORT})
        httpd.serve_forever()