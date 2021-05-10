from flask import Flask
from flask_testing import TestCase
import unittest
from cms import app
import requests
class MyTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app
    def test_server_is_up_and_running(self):
        response = requests.get()
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()
