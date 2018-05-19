import unittest
import requests

def to_answer(string):
    return string.strip('\n').strip('"')


class TestsWithRequests(unittest.TestCase):

    def test_is_responce_arrived(self):
        template_name = requests.post('http://localhost:7777/get_form?f1=asdasdasd@qweqwe.we&f2=2017-07-19')
        self.assertEqual(str(template_name), "<Response [200]>")

    def test_is_temp1(self):
        template_name = requests.post('http://localhost:7777/get_form?f1=asdasdasd@qweqwe.we&f2=2017-07-19')
        self.assertEqual(to_answer(template_name.text), 'temp1')

    @unittest.skip("Because of dict's special properties")
    def test_failure_match(self):
        template_name = requests.post('http://localhost:7777/get_form?f1=asdasdasd@qweqwe.we&f2=+7 916 243 32 03')
        self.assertEqual(to_answer(template_name.text), '{"f1": "email", "f2": "phone"}')


if __name__=="__main__":
    unittest.main()