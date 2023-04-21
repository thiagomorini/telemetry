import json

class Player:
    def __init__(self):
        self.id = None
        self.session_id = ''

    def get_player_data(self, username):
        self.username = username

        player_data = {
            'username': self.username,
            'session_id': self.session_id
        }
        return player_data

    def set_player_data(self, data):
        data_dict = json.loads(data)
        self.id = data_dict.get('id')
        self.username = data_dict.get('username')
        self.session_id = data_dict.get('session_id')
