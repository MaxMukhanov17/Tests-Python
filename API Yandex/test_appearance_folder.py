import unittest
import requests

class TestAPIYandex(unittest.TestCase):
    def setUp(self) -> None:
        print('===> setUp')

    def tearDown(self) -> None:
        print('===> tearDown')

    def test_appearance_folder(self):
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        TOKEN = 'AQAAAABb8nnZAADLW3ZCk3mPt0rxqBM39pD7aTs'
        HEADERS = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {TOKEN}'
        }
        PARAMS = {'path': '/'}
        info_folders = requests.get(url=URL, params=PARAMS, headers=HEADERS).json()['_embedded']['items']
        for info_folder in info_folders:
            name_folder = info_folder['name']
            if name_folder == 'Test':
                name_test = name_folder
        self.assertTrue(name_test == 'Test')


if __name__ == '__main__':
    unittest.main()