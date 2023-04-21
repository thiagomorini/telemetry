from socket_handler import SocketHandler
import requests
import json

class PlayerHandler(SocketHandler):
    def save_data(self):
        if self.method == 'POST':
            response = requests.post(self.url, data=json.dumps(self.data), headers=self.headers)

            if response.status_code == 201:
                print(f'Player data saved successfully (code: {response.status_code}).')
            else:
                print(f'Failed to save player data (code: {response.status_code}).')
        elif self.method == 'GET':
            response = requests.get(self.url, data=json.dumps(self.data), headers=self.headers)

            if response.status_code == 200:
                print(f'Player data was successfully retrieved (code: {response.status_code}).')
            else:
                print(f'Failed to get player data (code: {response.status_code}).')

        return response
