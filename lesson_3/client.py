'''
Задание 3
1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
клиент отправляет запрос серверу; сервер отвечает соответствующим кодом результата.
Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.

Функции клиента:
сформировать presence-сообщение;
отправить сообщение серверу;
получить ответ сервера;
разобрать сообщение сервера;
параметры командной строки скрипта client.py <addr> [<port>]:
addr — ip-адрес сервера;
port — tcp-порт на сервере, по умолчанию 7777.
'''
import json
import sys
import time
from socket import *


def create_connection(hostname: str = 'localhost', port: int = 7777):
    connection = socket(AF_INET, SOCK_STREAM)
    connection.connect((hostname, port))
    print(f'Open connection : {hostname} : {port}')
    return connection


def close_connection(connect: socket):
    connect.close()
    print('connection closed')


def send_message(connect: socket, message: dict):
    decode_message = json.dumps(message).encode('utf-8')
    try:
        connect.send(decode_message)
        print('Message was sent')
    except:
        print('Something went wrong')


def create_presence(account_name='Guest'):
    action = {
        'action': 'presence',
        'time': time.ctime(time.time()),
        'user': account_name,
    }
    print(f'message was created: {action}')
    return action


def get_response(connect: socket):
    encoded_response = connect.recv(1024)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode('utf-8')
        response = json.loads(json_response)
        print(f'Кesponse was got: {response}')
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def verify_message(message):
    if 'response' in message:
        if message['response'] == 200:
            return f'200 : {message}'
        print('400 : Something went wrong')
    raise ValueError


def main():

    try:
        hostname = sys.argv[1]
        port = int(sys.argv[2])
        if port < 1024 or port > 65535:
            raise ValueError
    except IndexError:
        hostname = '127.0.0.1'
        port = 7777
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    connection = create_connection(hostname, port)
    send_message(connection, create_presence())
    try:
        answer = verify_message(get_response(connection))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Decoding is failed')
    close_connection(connection)


if __name__ == '__main__':
    main()
