import pytest
from pytest_mock import MockerFixture
from common_tests import CommonTests
from fastapi.testclient import TestClient
from .mock import GET_USER_DATABASE_RESPONSE, GET_USERS_RESPONSE


class TestGetUser(CommonTests):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/usuarios'
    
    def test_get_users_success(self, client: TestClient, mocker: MockerFixture):
        mocker.patch(
            'database.Database.get_usuarios'
        ).return_value = GET_USER_DATABASE_RESPONSE
        response = client.get(self.url)
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        print('response_json', response_json)
        self.assertEqual(len(response_json), 1)
        self.assertListEqual(response_json, GET_USERS_RESPONSE)

    def test_get_user_success(self, client: TestClient):
        response = client.get(f'{self.url}/1/')
        print('response_text', response.text)
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        print('response_json', response_json)
        self.assertListEqual(response_json, GET_USERS_RESPONSE[0])
