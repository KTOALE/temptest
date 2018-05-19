import unittest
import requests

def to_answer(string):
    return string.strip('\n').strip('"')


class TestsWithRequests(unittest.TestCase):

    def test_is_responce_arrived(self):
        template_name = requests.post('http://localhost:7777/get_form?'
                                      'f1=asdasdasd@qweqwe.we&f2=2017-07-19')
        self.assertEqual(str(template_name), "<Response [200]>")

    def test_is_temp1(self):
        template_name = requests.post('http://localhost:7777/get_form?'
                                      'f1=asdasdasd@qweqwe.we&f2=2017-07-19')
        self.assertEqual(to_answer(template_name.text), 'temp1')

    @unittest.skip("Because of python's dicts special properties(prop. of unordered)")
    def test_failure_match(self):
        template_name = requests.post('http://localhost:7777/get_form?'
                                      'f1=asdasdasd@qweqwe.we&f2=8 916 333 33 33')
        self.assertEqual(to_answer(template_name.text), '{"f1": "email", "f2": "phone"}')

    def test_is_temp9(self):
            template_name = requests.post('http://localhost:7777/get_form?'
                                          'f1=8 916 222 22 22&f2=8 916 333 33 33')
            self.assertEqual(to_answer(template_name.text), 'temp9')

    def test_is_temp12(self):
        template_name = requests.post('http://localhost:7777/get_form?'
                                      'f1=asd@qwe.we&f2=asd@qwe.we&f3=8 916 333 33 33&'
                                      'f=asdasd&2=aasd@qwe.we')
        self.assertEqual(to_answer(template_name.text), 'temp12')


if __name__=="__main__":
    unittest.main()