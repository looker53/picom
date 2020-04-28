import requests


class SMUploader:

    def __init__(self):
        self.session = requests.Session()

    def upload_sm(self, file):
        api_addr = 'https://sm.ms/api/v2'
        upload_api = '/upload'
        url = api_addr + upload_api

        files = {
            "smfile": open(file, 'rb')
        }

        res = self.session.post(url, files=files)
        resp = res.json()
        code = resp.get('code')

        if code == 'image_repeated':
            url = resp.get["data"]
            return url
        elif code == 'success':
            return resp["data"]["url"]
        raise ValueError("API Error")

    def close(self):
        self.session.close()
