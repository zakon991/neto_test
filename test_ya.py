import unittest
import requests


class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.token = 'token'
        self.base_url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def test_positive_create_folder(self):
        folder_path = "/test_positive"
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {"path": folder_path}

        response = requests.put(self.base_url, headers=headers, params=params)

        self.assertEqual(response.status_code, 201)

    def test_invalid_token(self):
        invalid_token = 'invalid_token'
        folder_path = "/test_negative_invalid_token"
        headers = {'Authorization': f'OAuth {invalid_token}'}
        params = {"path": folder_path}

        response = requests.put(self.base_url, headers=headers, params=params)

        self.assertNotEqual(response.status_code, 201)

    def test_existing_folder(self):
        folder_path = "/test_negative_existing_folder"
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {"path": folder_path}

        requests.put(self.base_url, headers=headers, params=params)
        response = requests.put(self.base_url, headers=headers, params=params)

        self.assertNotEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
