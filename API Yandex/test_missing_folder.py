import unittest
import requests

class TestAPIYandex(unittest.TestCase):
    def setUp(self) -> None:
        print('===> setUp')

    def tearDown(self) -> None:
        print('===> tearDown')

    def test_status_code(self):
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        TOKEN = 'AQAAAABb8nnZAADLW3ZCk3mPt0rxqBM39pD7aTs'
        HEADERS = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {TOKEN}'
        }
        PARAMS = {'path': '/'}
        response = requests.get(url=URL, params=PARAMS, headers=HEADERS)
        response.raise_for_status()
        self.assertTrue(response.status_code == 401)


if __name__ == '__main__':
    unittest.main()