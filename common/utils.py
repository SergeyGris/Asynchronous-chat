"""Утилиты"""
import socket
import sys
import json
from ipaddress import ip_address
from subprocess import Popen, PIPE
from tabulate import tabulate


from common.variables import MAX_PACKAGE_LENGTH, ENCODING
from errors import IncorrectDataRecivedError, NonDictInputError
from decos import log

sys.path.append('../')


@log
def get_message(client):
    """
    Утилита приёма и декодирования сообщения принимает байты выдаёт словарь,
    если приняточто-то другое отдаёт ошибку значения
    :param client:
    :return:
    """
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        else:
            raise IncorrectDataRecivedError
    else:
        raise IncorrectDataRecivedError


@log
def send_message(sock, message):
    """
    Утилита кодирования и отправки сообщения
    принимает словарь и отправляет его
    :param sock:
    :param message:
    :return:
    """
    if not isinstance(message, dict):
        raise NonDictInputError
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)


def host_ping(list_ip, timeout=500, requests=1):
    result = {'Доступные узлы': [], 'Недоступные узлы': []}
    for address in list_ip:
        try:
            address = ip_address(address)
        except ValueError:
            address = ip_address(socket.gethostbyname_ex(address)[2][0])

        proc = Popen(f"ping {address} -w {timeout} -n {requests}", shell=False, stdout=PIPE)
        proc.wait()

        if proc.returncode == 0:
            result['Доступные узлы'].append(address)
            print(f'{address} - Узел доступен')
        else:
            result['Недоступные узлы'].append(address)
            print(f'{address} - Узел недоступен')

    return result

'''
192.168.0.1 - Узел доступен
94.100.180.200 - Узел недоступен
{'Доступные узлы': IPv4Address('192.168.0.1'), 'Недоступные узлы': IPv4Address('94.100.180.200')}
'''

def host_range_ping():
    start = input('Введите ip: ')
    try:
        las_oct = int(start.split('.')[3])
    except Exception as e:
        print(e)
    while True:
        end = input('Сколько адресов проверить?: ')
        if not end.isnumeric():
            print('Необходимо ввести число: ')
        else:
            if (las_oct+int(end)) > 254:
                print(f"Можем менять только последний октет, т.е. "
                      f"максимальное число хостов для проверки: {254-las_oct}")
            else:
                break

    host_list = []
    [host_list.append(str(ip_address(start)+x)) for x in range(int(end))]

    return host_ping(host_list)
'''
192.168.0.1 - Узел доступен
192.168.0.2 - Узел недоступен
192.168.0.3 - Узел недоступен
192.168.0.4 - Узел недоступен
192.168.0.5 - Узел недоступен
{'Доступные узлы': IPv4Address('192.168.0.1'), 'Недоступные узлы': IPv4Address('192.168.0.5')}

'''
def host_range_ping_tab():
    ips = host_range_ping()

    print(tabulate([ips], headers='keys', stralign="center", tablefmt='grid'))

'''
192.168.0.1 - Узел доступен
192.168.0.2 - Узел недоступен
192.168.0.3 - Узел недоступен
+------------------------------+----------------------------------------------------------+
|        Доступные узлы        |                     Недоступные узлы                     |
+==============================+==========================================================+
| [IPv4Address('192.168.0.1')] | [IPv4Address('192.168.0.2'), IPv4Address('192.168.0.3')] |
+------------------------------+----------------------------------------------------------+

'''