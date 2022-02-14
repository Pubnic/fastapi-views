import pytest
from common_tests import CommonTests
from fastapi.testclient import TestClient


class TestGetUser(CommonTests):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/usuarios/'
        self.body = {'name': 'Anna', 'age': 28}
    
    def test_create_user_success(self, client: TestClient):
        response = client.post(self.url, json=self.body)
        print('status_code', response.status_code)
        print('response_text', response.text)
        self.assertEqual(response.status_code, 201)
        response_json = response.json()
        usuario_criado = {
            'id': 3,
            **self.body
        }
        self.assertDictEqual(response_json, usuario_criado)
