import json
import unittest
from socket import *

from lesson_3.client import create_presence, create_connection, send_message, verify_message


class TestClient(unittest.TestCase):
    test_message = {
        'action': 'presence',
        'time': 1,
        'user': 'Guest',
    }

    test_response = {
        'response': 200
    }

    def test_connection(self):
        test_connection = create_connection()
        self.assertIsInstance(test_connection, socket)
        test_connection.close()

    def test_send_message(self):
        test_connection = create_connection()
        test_rez = send_message(test_connection, self.test_message)
        test_connection.close()
        rez = 'Message was sent'

        self.assertEqual(rez, test_rez)

    def test_create_presence(self):
        test = create_presence()
        test['time'] = 1
        self.assertEqual(self.test_message, test)

    def test_verify_message(self):
        test = verify_message(self.test_response)
        response = f'200 : {self.test_response}'

        self.assertEqual(response, test)



if __name__ == '__main__':
    unittest.main()
