# store hardcoded data that can be accessed through a REST  call in JSON format
import json, socketserver, http.server, requests

PORT = 5000

isStorageRunning = True

#random generated dummy data
data = [
    {
        'question': 'What is the capital of France?',
        'answer': 'Paris',
        'alternate_answers': ['France', 'Madrid', 'Rome', 'Berlin']
    },
    {
        'question': 'What is the capital of United States?',
        'answer': 'Washington',
        'alternate_answers': ['New York', 'Ontario', 'Las Vegas', 'Los Angeles']
    },
    {
        'question': 'What is the capital of Japan?',
        'answer': 'Tokyo',
        'alternate_answers': ['Kyoto', 'Hiroshima', 'Osaka', 'Sapporo']
    }
]

class Storage(http.server.SimpleHTTPRequestHandler):

    iterator = 0

    def do_GET(self):
        print(f"Requested path: {self.path}")
        # round robyn with iterator that doesnt go out of bounds
        if self.path == "/data" or self.path.rstrip("/") == "/data":
            self.send_response(200)
            item = data[Storage.iterator]
            print(json.dumps(item))
            Storage.iterator = (Storage.iterator + 1) % len(data)

        elif self.path == "/status" or self.path.rstrip("/") == "/status":
            if isStorageRunning:
                self.send_response(200)
                print(json.dumps({"status": "running"}))
            else:
                self.send_response(500)
                print(json.dumps({"status": "down"}))

        else:
            # storage status not found or down
            self.send_response(404)
            print("404 Not Found")

    
if __name__ == '__main__':
    # TCPServer constructor("empty tuple that listens to all interfaces, PORT number")
    with socketserver.TCPServer(("", PORT), Storage) as httpd:
        print(f"Running on port ", {PORT})
        httpd.serve_forever()
        



    

    