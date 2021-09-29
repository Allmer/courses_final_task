from helpers.api_calls import ApiTesting
import allure


@allure.story("Test API requests")
def test_user_add_login_getdata_logout_delete():
    with allure.step("Create User"):
        api = ApiTesting()
        api.create_user()
    with allure.step("User login"):
        api.user_login()
    with allure.step("Collecting user data"):
        api.collect_user_data()
    with allure.step("User logout"):
        api.user_logout()
    with allure.step("Delete User"):
        api.user_delete()
