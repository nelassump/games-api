import requests
import pytest


class TestGamesRequests:
    url_base_games = 'http://127.0.0.1:8000/api/v2/games/'
    headers = {'Authorization': 'Token 4e8c65b8d9ef369c5337c0ee66c369a8dab6a278'}

    def test_get_games(self):
        response = requests.get(url=self.url_base_games, headers=self.headers)

        assert response.status_code==200

    def test_get_game(self):
        response = requests.get(url=f'{self.url_base_games}3/', headers=self.headers)

        assert response.status_code == 200

    @pytest.fixture(name="message")
    def test_post_game(self):
        new = {
        "title": "Jogo teste",
        "url": "http://pudim.com.br/11/"
        }
        response = requests.post(url=self.url_base_games, headers=self.headers, data=new)

        assert response.status_code == 201
        assert response.json()['title'] == new['title']
        return response.json()

    def test_delete_game(self, message):
        response = requests.delete(url=f"{self.url_base_games}{message['id']}/", headers=self.headers)

        assert response.status_code == 204

    def test_put_game(self):
        update = {
            "title": "Jogo teste 2",
            "url": "http://pudim.com.br/2/"
        }
        response = requests.put(url=f'{self.url_base_games}3/', headers=self.headers, data=update)

        assert response.status_code==200
        assert response.json()['url'] == update['url']    
    