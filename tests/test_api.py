from helpers.api_client import ApiTesting
import helpers.testdata
import allure


@allure.story("Test API requests")
def test_user_add_login_getdata_logout_delete():

    with allure.step(f"Create User with id {helpers.testdata.user_id},"
                     f"username {helpers.testdata.user_name}"):
        api = ApiTesting()
        api.create_user()

    with allure.step(f"User {helpers.testdata.user_name} login"):
        api.user_login()

    with allure.step("Collecting user data"):
        api.collect_user_data()

    with allure.step(f"User {helpers.testdata.user_name} logout"):
        api.user_logout()

    with allure.step(f"Delete {helpers.testdata.user_name} User"):
        api.user_delete()
