import unittest
import requests
from test import *

class TestsWithRequests(unittest.TestCase):

    def is_temp1(self):
        template = requests.post('http://localhost:7777/get_form?f1=asdasdasd@qweqwe.we&f2=2017-07-19')
        self.assertEqual(template,'temp1')

if __name__=="__main__":
    unittest.main()