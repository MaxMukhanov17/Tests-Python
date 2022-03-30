import unittest
from unittest.mock import patch
from main import get_shelf


class TestFunctionsAccounting(unittest.TestCase):  
    def setUp(self) -> None:
        print('===> setUp')

    def tearDown(self) -> None:
        print('===> tearDown')

    @patch('main.input', return_value = '11-2')
    def test_get_shelf(self, mock_input):
        directories = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': []
            }
        self.assertMultiLineEqual(get_shelf(directories), '1')

if __name__ == '__main__':
    unittest.main()