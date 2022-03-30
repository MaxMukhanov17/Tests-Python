import unittest
from unittest.mock import patch
from main import get_name


class TestFunctionsAccounting(unittest.TestCase):  
    def setUp(self) -> None:
        print('===> setUp')

    def tearDown(self) -> None:
        print('===> tearDown')

    @patch('main.input', return_value = '10006')
    def test_get_shelf(self, mock_input):
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
            ]
        self.assertEqual(get_name(documents), 'Аристарх Павлов')

if __name__ == '__main__':
    unittest.main()