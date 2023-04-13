import unittest

from lesson_3.server import verify_client_message


class TestServer(unittest.TestCase):

    def test_verify_client_message(self):
        test_message = {
            'action': 'presence',
            'time': 1,
            'user': 'Guest',
        }
        test = verify_client_message(test_message)
        response = {
            'response': 200
        }

        self.assertEqual(response, test)

    def test_verify_client_message2(self):
        test_message = {}

        test = verify_client_message(test_message)
        response = {
            'response': 400,
        }

        self.assertEqual(response, test)


if __name__ == '__main__':
    unittest.main()
