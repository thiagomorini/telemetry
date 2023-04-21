import datetime
import math

MIN_DISTANCE = 1

class Telemetry:
    def __init__(self):
        self.previous_position = (0, 0, 0)

    def get_telemetry_data(self, player, position_x, position_y, position_z, keys_pressed):
        self.player = player
        self.datetime = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%dZ')
        self.position_x = '{:.2f}'.format(position_x)
        self.position_y = '{:.2f}'.format(position_y)
        self.position_z = '{:.2f}'.format(position_z)
        
        if len(keys_pressed) == 0:
            self.keys_pressed = '<NONE>'
        else:
            self.keys_pressed = keys_pressed

        telemetry_data = {
            'player': self.player,
            'datetime': self.datetime,
            'position_x': self.position_x,
            'position_y': self.position_y,
            'position_z': self.position_z,
            'keys_pressed': self.keys_pressed
        }
        return telemetry_data

    def check_distance(self, x, y, z):
        current_position = (x, y, z)

        distance = math.sqrt(
            (current_position[0] - self.previous_position[0])**2 +
            (current_position[1] - self.previous_position[1])**2 +
            (current_position[2] - self.previous_position[2])**2
        )

        if distance > MIN_DISTANCE:
            self.previous_position = current_position
            return True
        else:
            return False
        