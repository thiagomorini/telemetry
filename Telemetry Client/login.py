from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QDialog
from PyQt5.QtCore import pyqtSignal

class Login(QDialog):
    login_closed  = pyqtSignal()

    def __init__(self, client, player):
        super().__init__()
        self.player = player
        self.client = client
        self.initUI()

    def initUI(self):
        # Label
        self.label = QLabel('Username:', self)
        self.label.move(20, 30)

        # Input
        self.input = QLineEdit(self)
        self.input.move(90, 26)

        # Button
        self.button = QPushButton('Send', self)
        self.button.move(240, 24)
        self.button.clicked.connect(self.send_username)
        
        # Window
        self.setGeometry(300, 300, 350, 80)
        self.setWindowTitle('Login')
        self.show()

    def send_username(self):
        self.username = self.input.text()
        
        self.player_data = self.player.get_player_data(self.username)
        response = self.client.send_data(self.player_data)
        self.player.set_player_data(response)

        self.done(QDialog.Accepted)
