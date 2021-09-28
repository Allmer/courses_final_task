import psycopg2
from pages.main_page import MainPage
from pages.admin_login_page import AdminLoginPage
from pages.admin_page import AdminPage
from pages.groups_page import GroupsPage
#from helpers.db_query import do_insert_group, do_delete_group

# Group name parameter
created_group = "Third"
# postgres db connection params
myConnection = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='postgres')


def test_tc_1(browser, add_bd_group_and_delete_group):

    # Open app
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.should_be_main_page()

    # Open admin panel
    main_page.open_admin_page()
    admin_login_page = AdminLoginPage(browser)
    admin_login_page.should_be_admin_login_page()
    admin_login_page.login_to_admin_account("yaroslav", "123456Aa!")
    admin_page = AdminPage(browser)
    admin_page.should_be_admin_page()
    admin_page.open_groups_page()
    groups_page = GroupsPage(browser)
    groups_page.should_be_groups_page()

    # Check that new group is displayed
    groups_page.search_for_group(created_group)
    groups_page.check_search_results(created_group)

