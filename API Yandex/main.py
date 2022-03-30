import requests

class YaUpload:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self):
        create_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params_get = {'path': '/'}
        response = requests.get(
            url=create_url,
            headers=headers,
            params=params_get
        )
        info_folders = response.json()['_embedded']['items']
        for info_folder in info_folders:
            name_folder = info_folder['name']
            if name_folder == 'Test':
                continue
            else:
                params = {'path': '/Test'}
                requests.put(url=create_url, params=params, headers=headers)


if __name__ == '__main__':
    token = 'AQAAAABb8nnZAADLW3ZCk3mPt0rxqBM39pD7aTs'
    uploader = YaUpload(token)
    uploader.create_folder()
