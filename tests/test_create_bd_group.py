from pages.main_page import MainPage
from pages.admin_login_page import AdminLoginPage
from pages.admin_page import AdminPage
from pages.groups_page import GroupsPage
from helpers.testdata import AdminCreds, CreateBDGroup
from helpers.db_client import DB
import allure


@allure.story("Create group in BD "
              "and check in admin panel if new group is displayed")
def test_add_group_check_group(browser, delete_group):

    with allure.step(f"Create group {CreateBDGroup.group_name_tcbg}"
                     f" in DB table"):
        db = DB()
        db.do_insert_group(CreateBDGroup.group_name_tcbg)

    with allure.step("Open app"):
        main_page = MainPage(browser)
        main_page.open_main_page()
        main_page.should_be_main_page()

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

    with allure.step("Open Groups page in admin panel"):
        admin_page.open_groups_page()
        groups_page = GroupsPage(browser)
        groups_page.should_be_groups_page()

    with allure.step("Check if BD added group is displayed"):
        groups_page.search_for_group(CreateBDGroup.group_name_tcbg)
        groups_page.check_search_results(CreateBDGroup.group_name_tcbg)
