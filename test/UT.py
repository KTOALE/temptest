import unittest
import requests

def to_answer(string):
    return string.strip('\n').strip('"')


class TestsWithRequests(unittest.TestCase):

    def test_is_request_success(self):
        template_name = requests.post('http://localhost:7777/')
        self.assertEqual(to_answer(template_name.text), "HERE WE ARE")

    def test_is_temp1(self):
        template_name = requests.post('http://localhost:7777/get_form?f1=asdasdasd@qweqwe.we&f2=2017-07-19')
        self.assertEqual(to_answer(template_name.text), 'temp1')



if __name__=="__main__":
    unittest.main()