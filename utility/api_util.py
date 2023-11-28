import requests


class ApiUtility:
    def __init__(self):
        self.host = 'https://api.github.com/'
        self.headers = {
            'Content-Type': 'application/json'
        }

    def search_repositories(self, input_text):
        url = self.host + f'search/repositories?q={input_text}&sort=stars&order=desc&per_page=100000'
        resp = requests.get(url=url, headers=self.headers)
        assert resp.status_code == 200, f'Failed to search repos {resp.text}'
        return resp.json()
