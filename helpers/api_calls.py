import requests
import json


class ApiTesting:
    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2/user"
        self.request_data = {
            "id": 987,
            "username": "Yaroslav",
            "firstName": "Asd",
            "lastName": "Dsa",
            "email": "test@example.com",
            "password": "123456",
            "phone": "123456",
            "userStatus": 0
            }
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }

    # User creation
    def create_user(self):

        response = requests.post(self.base_url, data=json.dumps(self.request_data), headers=self.headers)

        try:
            response.status_code
        except requests.exceptions.HTTPError as e:
            print(f"Error: {e}")
        assert response.status_code == 200

    # User login
    def user_login(self):
        username = self.request_data["username"]
        password = self.request_data["password"]
        url = self.base_url + "/login?username=" + username + "&password=" + password

        response = requests.get(url, headers=self.headers)

        try:
            response.status_code
        except requests.exceptions.HTTPError as e:
            print(f"Error: {e}")
        assert response.status_code == 200

    # Collecting user info
    def collect_user_data(self):
        username = self.request_data["username"]
        url = self.base_url + "/" + username

        response = requests.get(url, headers=self.headers)

        try:
            response.status_code
        except requests.exceptions.HTTPError as e:
            print(f"Error: {e}")
        assert response.status_code == 200

    # User logout
    def user_logout(self):
        url = self.base_url + "/logout"

        response = requests.get(url, headers=self.headers)

        try:
            response.status_code
        except requests.exceptions.HTTPError as e:
            print(f"Error: {e}")
        assert response.status_code == 200

    # User deletion
    def user_delete(self):
        username = self.request_data["username"]
        url = self.base_url + "/" + username

        response = requests.delete(url, headers=self.headers)

        try:
            response.status_code
        except requests.exceptions.HTTPError as e:
            print(f"Error: {e}")
        assert response.status_code == 200
