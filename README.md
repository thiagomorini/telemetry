# Telemetry

This is a concept project for a telemetry server built with Django REST Framework, Socket, and Pygame. The client allows real-time telemetry sending of a 3D game to the Socket server, and a frontend in a browser allows telemetry visualization. The project is divided into four parts: the API server, the Socket server, the Pygame client, and the frontend for visualization.

## Used technologies

- Python 3.11
- Django 4.2
- Django CORS 3.14.0
- Django REST Framework 3.14.0
- Game Engine pygame 2.1.3
- PyQt5 5.15.9

## Installation and execution

Clone the repository to your computer:

```
git clone https://github.com/thiagomorini/telemetry.git
```

Make sure that Python 3.8 or higher is installed on your machine. If it is not, you can install it using the following command:

```
sudo apt install python3
```

### API Server, Socket Server, and the Frontend for telemetry visualization

To run the API server, follow these steps:

1. Access the project directory: Telemetry Server.

2. Install the project dependencies.

3. Run the database migrations:

```
python manage.py migrate
```

4. Run the server:

```
python manage.py runserver
```

5. Access the project's API in your browser through the address http://127.0.0.1:8000/api/telemetry/

6. Access the project's frontend in your browser through the address http://127.0.0.1:8000/telemetry/

To run the Socket server, follow these steps:

1. Access the project directory: Telemetry Server\game_server.

2. Run the server:

```
python socket_server.py  
```

### Socket Client with the game

To run the Socket Client, follow these steps:

1. Access the project directory: Telemetry Client.

2. Install the project dependencies.

3. Run the client:

```
python main.py  
```

## Contribution

You can contribute to the project in several ways:

1. Reporting bugs and issues on Github.
2. Making pull requests with fixes and new features.
3. Sharing the project and encouraging other developers to use it.

## Licence
This project is distributed under the MIT license.

## Contact
You can contact me anytime you have questions or suggestions for improvement.
