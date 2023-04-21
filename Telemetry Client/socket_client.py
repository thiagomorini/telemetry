import socket
import json

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.host, self.port))
        print(f"Connection to server {self.host}:{self.port} established.")

    def send_data(self, data):
        data_json = json.dumps(data).encode('utf-8')
        self.sock.sendall(data_json)
        response = self.sock.recv(1024)

        if response:
            response_str = response.decode('utf-8')
            return response_str
        else:
            print("No response from server")
            return ""

    def disconnect(self):
        self.sock.close()
        print(f"Connection to server {self.host}:{self.port} terminated.")
