import socket
import threading
import json
from telemetry_handler import TelemetryHandler
from player_handler import PlayerHandler

CREATE_PLAYER_URL = 'http://127.0.0.1:8000/api/players/create/'
GET_PLAYER_URL = 'http://127.0.0.1:8000/api/players/{}/'
CREATE_TELEMETRY_URL = 'http://127.0.0.1:8000/api/telemetry/create/'

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(5)
        print(f'The server is listening on {host}:{port}.')

    def start(self):
        while True:
            conn, addr = self.sock.accept()
            client_thread = threading.Thread(target=self.handle_client_connection, args=(conn, addr))
            client_thread.start()

    def handle_client_connection(self, conn, addr):
        print(f'New connection established: {addr[0]}:{addr[1]}')
        while True:
            data = conn.recv(1024)
            if not data:
                print(f'{addr[0]}:{addr[1]} closed connection.')
                break
            print(f'Data received from {addr[0]}:{addr[1]}: {data.decode("utf-8")}')
            
            # Determine which handler to use based on the received data
            if b'position_x' in data:
                self.telemetry_handler = TelemetryHandler(CREATE_TELEMETRY_URL, 'POST')
                handler = self.telemetry_handler
            else:
                player_json = json.loads(data)

                if len(player_json['session_id']) == 0:
                    self.player_handler = PlayerHandler(CREATE_PLAYER_URL, 'POST')
                else:
                    url = GET_PLAYER_URL.format(player_json['session_id'])
                    self.player_handler = PlayerHandler(url, 'GET')

                handler = self.player_handler

            handler.handle_socket_data(data.decode('utf-8'))
            response = handler.save_data()

            # Send the response back to the client
            conn.sendall(response.content)

        conn.close()

if __name__ == '__main__':
    server = Server('localhost', 5002)
    server.start()
