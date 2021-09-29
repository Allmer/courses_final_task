from helpers.api_calls import ApiTesting


def test_user_add_login_getdata_logout_delete():
    api = ApiTesting()
    api.create_user()
    api.user_login()
    api.collect_user_data()
    api.user_logout()
    api.user_delete()
