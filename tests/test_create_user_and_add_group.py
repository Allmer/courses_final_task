from pages.main_page import MainPage
from pages.admin_login_page import AdminLoginPage
from pages.admin_page import AdminPage
from pages.add_user_page import AddUserPage
from pages.change_user_page import ChangeUserPage
from helpers.testdata import AdminCreds, CreateUserAndAddGroup


def test_add_user_to_group(browser, create_user_add_group_check_usergroup):

    # Open app
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.should_be_main_page()

    # Open admin panel
    main_page.open_admin_page()
    admin_login_page = AdminLoginPage(browser)
    admin_login_page.should_be_admin_login_page()
    admin_login_page.login_to_admin_account(
        AdminCreds.admin_login,
        AdminCreds.admin_password
    )
    admin_page = AdminPage(browser)
    admin_page.should_be_admin_page()

    # Add new user
    admin_page.open_user_page()
    add_user_page = AddUserPage(browser)
    add_user_page.should_be_add_user_page()
    add_user_page.create_user(
        CreateUserAndAddGroup.user_name,
        CreateUserAndAddGroup.user_password,
        CreateUserAndAddGroup.user_password
    )
    change_user_page = ChangeUserPage(browser)
    change_user_page.should_be_change_user_page()

    # Add group for the new user
    change_user_page.add_group_for_user()
    change_user_page.add_user_email(CreateUserAndAddGroup.user_email)
    change_user_page.click_on_save_button()
