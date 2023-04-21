import json

class SocketHandler:
    def __init__(self, url, method):
        self.url = url
        self.headers = {'Content-type': 'application/json'}
        self.buffer = ''
        self.method = method

    def handle_socket_data(self, data):
        self.buffer += data
        
        while True:
            try:
                index = self.buffer.index('}')
                json_str = self.buffer[:index+1]
                self.data = json.loads(json_str)
                self.buffer = self.buffer[index+1:].lstrip()
            except ValueError:
                break

    def save_data(self):
        raise NotImplementedError
