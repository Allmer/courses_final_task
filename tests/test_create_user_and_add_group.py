from pages.main_page import MainPage
from pages.admin_login_page import AdminLoginPage
from pages.admin_page import AdminPage
from pages.add_user_page import AddUserPage
from pages.change_user_page import ChangeUserPage
from helpers.testdata import AdminCreds, CreateUserAndAddGroup
from helpers.db_client import DB
import allure


@allure.story("Run app, open admin panel, create user, add user to group"
              "and check that user belongs to group in BD")
def test_add_user_to_group(browser, delete_user):

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

    with allure.step(f"Create new user with name"
                     f" {CreateUserAndAddGroup.user_name}"):
        add_user_page.create_user(
            CreateUserAndAddGroup.user_name,
            CreateUserAndAddGroup.user_password,
            CreateUserAndAddGroup.user_password
        )

    with allure.step("Open Change user page"):
        change_user_page = ChangeUserPage(browser)
        change_user_page.should_be_change_user_page()

    # Add group for the new user
    with allure.step(f"Select {CreateUserAndAddGroup.group_name_tcuaag}"
                     f"group for new user"):
        change_user_page.add_group_for_user()

    with allure.step(f"Add user email {CreateUserAndAddGroup.user_email}"):
        change_user_page.add_user_email(CreateUserAndAddGroup.user_email)

    with allure.step("Click on save button"):
        change_user_page.click_on_save_button()

    # Check that new user added to group in DB
    with allure.step(f"Find user {CreateUserAndAddGroup.user_name} by username and email in DB"):
        db = DB()
        db.do_find_user(
            CreateUserAndAddGroup.user_name,
            CreateUserAndAddGroup.user_email
        )

    with allure.step("Find user group in DB"):
        db.do_find_group_for_user(
            CreateUserAndAddGroup.user_email,
            CreateUserAndAddGroup.group_name_tcuaag
        )
