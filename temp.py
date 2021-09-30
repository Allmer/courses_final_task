import requests

headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
url = "https://petstore.swagger.io/v2/user/Yaroslav"

result = ""
while result != 200:
    response = requests.get(url, headers=headers)
    result = response.status_code
    print(result)
else:
    assert result == 200, f'Status code {result} is not eq 200'