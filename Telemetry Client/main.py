import sys
from PyQt5.QtWidgets import QApplication, QDialog
from player import Player
from game import Game
from socket_client import Client
from login import Login

if __name__ == "__main__":
    player = Player()

    client = Client('localhost', 5002)
    client.connect()

    app = QApplication(sys.argv)
    login = Login(client, player)
    if login.exec_() == QDialog.Accepted:
        # Success
        game = Game(client, player)
        game.run()
    else:
        # Fail
        sys.exit(0)

    client.disconnect()
