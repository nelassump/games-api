import requests


class TestGamesRequests:
    url_base_games = 'http://127.0.0.1:8000/api/v2/games/'
    headers = {'Authorization': 'Token 4e8c65b8d9ef369c5337c0ee66c369a8dab6a278'}

    def test_get_games(self):
        games = requests.get(url=self.url_base_games, headers=self.headers)

        assert games.status_code==200

    def test_get_game(self):
        game = requests.get(url=f'{self.url_base_games}3/', headers=self.headers)

        assert game.status_code == 200

    def test_post_game(self):
        new = {
        "title": "Jogo teste",
        "url": "http://pudim.com.br/9"
        }
        result = requests.post(url=self.url_base_games, headers=self.headers, data=new)

        assert result.status_code == 201
        assert result.json()['title'] == new['title']

    def test_delete_game(self):
        delete = requests.delete(url=f'{self.url_base_games}9/', headers=self.headers)

        assert delete.status_code == 204 and len(delete.text) == 0
    """
    aqui eu preciso criar uma validacao melhor para pegar o ID criado anteriormente e testar o delete nele
    """

    def test_put_game(self):
        update = {
            "title": "Jogo teste 2",
            "url": "http://pudim.com.br/2/"
        }
        result = requests.put(url=f'{self.url_base_games}3/', headers=self.headers, data=update)

        assert result.status_code==200
        assert result.json()['url'] == update['url']    
    