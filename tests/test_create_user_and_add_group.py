from pages.main_page import MainPage
from pages.admin_login_page import AdminLoginPage
from pages.admin_page import AdminPage
from pages.add_user_page import AddUserPage
from pages.change_user_page import ChangeUserPage
from helpers.testdata import AdminCreds, CreateUserAndAddGroup
import allure


@allure.story("Run app, open admin panel, create user, add user to group"
              "and check that user belongs to group in BD")
def test_add_user_to_group(browser, create_user_add_group_check_usergroup):

    # Open app
    with allure.step("Open app"):
        main_page = MainPage(browser)
        main_page.open_main_page()
        main_page.should_be_main_page()

    # Open admin panel
    with allure.step("Open admin panel login form"):
        main_page.open_admin_page()
        admin_login_page = AdminLoginPage(browser)
        admin_login_page.should_be_admin_login_page()

    with allure.step("Login to admin panel"):
        admin_login_page.login_to_admin_account(
            AdminCreds.admin_login,
            AdminCreds.admin_password
        )

    with allure.step("Open admin panel interface"):
        admin_page = AdminPage(browser)
        admin_page.should_be_admin_page()

    # Add new user
    with allure.step("Open User page in admin panel"):
        admin_page.open_user_page()
        add_user_page = AddUserPage(browser)
        add_user_page.should_be_add_user_page()

    with allure.step("Create new user"):
        add_user_page.create_user(
            CreateUserAndAddGroup.user_name,
            CreateUserAndAddGroup.user_password,
            CreateUserAndAddGroup.user_password
        )

    with allure.step("Open Change user page"):
        change_user_page = ChangeUserPage(browser)
        change_user_page.should_be_change_user_page()

    # Add group for the new user
    with allure.step("Select group for new user"):
        change_user_page.add_group_for_user()

    with allure.step("Add user email"):
        change_user_page.add_user_email(CreateUserAndAddGroup.user_email)

    with allure.step("Saving new user data"):
        change_user_page.click_on_save_button()
