import requests
import pytest

class TestEvaluationsRequests:
    url_base_evaluations = 'http://127.0.0.1:8000/api/v2/evaluations/'
    headers = {'Authorization': 'Token 4e8c65b8d9ef369c5337c0ee66c369a8dab6a278'}

    def test_get_evaluations(self):
        response = requests.get(url=self.url_base_evaluations, headers=self.headers)

        assert response.status_code==200

    def test_get_evaluation(self):
        response = requests.get(url=f'{self.url_base_evaluations}2/', headers=self.headers)

        assert response.status_code==200

    @pytest.fixture(name="message")
    def test_post_evaluation(self):
        new = {
        "game": 5,
        "name": "Teste",
        "email": "teste66@gmail.com",
        "comment": "Testando",
        "grade": 8
        }

        response = requests.post(url=self.url_base_evaluations, headers=self.headers, data=new)

        assert response.status_code == 201
        assert response.json()['name'] == new['name']
        return response.json()

    def test_delete_evaluation(self, message):
        response = requests.delete(url=f"{self.url_base_evaluations}{message['id']}/", headers=self.headers)

        assert response.status_code == 204