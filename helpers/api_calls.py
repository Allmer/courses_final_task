import requests
import json


# User creation
def create_user(request_data, base_url):

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.post(base_url, data=json.dumps(request_data), headers=headers)

    try:
        response.status_code
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
    assert response.status_code == 200


# User login
def user_login(request_data, base_url):
    username = request_data["username"]
    password = request_data["password"]
    url = base_url + "/login?username=" + username + "&password=" + password
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    try:
        response.status_code
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
    assert response.status_code == 200


# Collecting user info
def collect_user_data(request_data, base_url):
    username = request_data["username"]
    url = base_url + "/" + username
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    try:
        response.status_code
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
    assert response.status_code == 200


# User logout
def user_logout(base_url):
    url = base_url + "/logout"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    try:
        response.status_code
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
    assert response.status_code == 200


# User deletion
def user_delete(request_data, base_url):
    username = request_data["username"]
    url = base_url + "/" + username
    url = "https://petstore.swagger.io/v2/user/Allmer"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.delete(url, headers=headers)

    try:
        response.status_code
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
    assert response.status_code == 200
