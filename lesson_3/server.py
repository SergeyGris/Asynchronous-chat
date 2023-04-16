'''
Задание 3
1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
клиент отправляет запрос серверу; сервер отвечает соответствующим кодом результата.
Клиент и сервер должны быть реализованы в виде отдельных скриптов,содержащих соответствующие функции.

Функции сервера:
принимает сообщение клиента;
формирует ответ клиенту;
отправляет ответ клиенту;
имеет параметры командной строки:
-p <port> — TCP-порт для работы (по умолчанию использует 7777);
-a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
'''
import json
import sys
from socket import *


from lesson_3.client import get_response, send_message


def verify_client_message(message):

    if 'action' in message:
        return {
            'response': 200
        }


    return {
        'response': 400,
    }


def main():
    try:
        if '-p' in sys.argv:
            port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            port = 7777
        if port < 1024 or port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            hostname = sys.argv[sys.argv.index('-a') + 1]
        else:
            hostname = '127.0.0.1'

    except IndexError:
        print('После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    connection = socket(AF_INET, SOCK_STREAM)
    connection.bind((hostname, port))

    connection.listen(5)

    while True:
        client, client_address = connection.accept()
        try:
            client_message = get_response(client)
            print(f'Client message{client_message}')

            response = verify_client_message(client_message)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Incorrect message')
            client.close()


if __name__ == '__main__':
    main()
