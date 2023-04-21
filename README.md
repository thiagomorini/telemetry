# Telemetry

Este é um projeto conceito de um servidor de telemetria construído com Django REST Framework, Socket e Pygame. O client permite o envio de telemetria de um jogo em 3D em tempo real para o server Socket, e um frontend em um navegador permite a visualização da telemetria. O projeto é dividido em quatro partes: o servidor da API, o servidor Socket, o cliente Pygame e o frontend para a visualização.

## Tecnologias utilizadas

- Python 3.11
- Django 4.2
- Django CORS 3.14.0
- Django REST Framework 3.14.0
- Game Engine pygame 2.1.3
- PyQt5 5.15.9

## Instalação e execução

Clone o repositório para o seu computador:

```
git clone https://github.com/thiagomorini/telemetry.git
```

Certifique-se de que o Python 3.8 ou superior esteja instalado em sua máquina. Caso não esteja, você pode instalá-lo usando o seguinte comando:

```
sudo apt install python3
```

### API Server, Socket Server e o Frontend para a visualização das telemetrias

Para executar o servidor da API, siga os seguintes passos:

1. Acesse o diretório do projeto: Telemetry Server.

2. Instale as dependências do projeto.

3. Execute as migrações do banco de dados:

```
python manage.py migrate
```

4. Execute o servidor:

```
python manage.py runserver
```

5. Acesse a API do projeto em seu navegador através do endereço http://127.0.0.1:8000/api/telemetry/

6. Acesse o frontend do projeto em seu navegador através do endereço http://127.0.0.1:8000/telemetry/

Para executar o servidor Socket, siga os seguintes passos:

1. Acesse o diretório do projeto: Telemetry Server\game_server

2. Execute o servidor:

```
python socket_server.py  
```

### Socket Client com o jogo

Para executar o Socket Client, siga os seguintes passos:

1. Acesse o diretório do projeto: Telemetry Client.

2. Instale as dependências do projeto.

3. Execute o client:

```
python main.py  
```







## Contribuição

Você pode contribuir com o projeto de várias formas:

1. Reportando bugs e problemas no Github.
2. Fazendo pull requests com correções e novas funcionalidades.
3. Compartilhando o projeto e incentivando outros desenvolvedores a usá-lo.

## Licença
Este projeto é distribuído sob a licença MIT.

## Contato
Você pode entrar em contato comigo sempre que tiver alguma dúvida ou sugestão de melhorias.
