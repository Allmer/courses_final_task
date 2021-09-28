import helpers.api_calls

base_url = "https://petstore.swagger.io/v2/user"
request_data = {
            "id": 987,
            "username": "Allmer",
            "firstName": "Asd",
            "lastName": "Dsa",
            "email": "test@example.com",
            "password": "123456",
            "phone": "123456",
            "userStatus": 0
            }


def test_tc_3():
    helpers.api_calls.create_user(request_data, base_url)
    helpers.api_calls.user_login(request_data, base_url)
    helpers.api_calls.collect_user_data(request_data, base_url)
    helpers.api_calls.user_logout(base_url)
    helpers.api_calls.user_delete(request_data, base_url)
