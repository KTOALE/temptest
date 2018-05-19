import unittest
import requests

class TestsWithRequests(unittest.TestCase):

    def is_temp1(self):
        template = requests.post('http://localhost:7777/getform?f1=asdasdasd@qweqwe.we&f2=2017-07-19')
        self.assertEqual(template,'temp1')

if __name__=="__main__":
    unittest.main()