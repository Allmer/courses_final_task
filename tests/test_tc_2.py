import psycopg2
from pages.main_page import MainPage
from pages.admin_login_page import AdminLoginPage
from pages.admin_page import AdminPage
from pages.add_user_page import AddUserPage
from pages.change_user_page import ChangeUserPage
from db_query import do_find_user, do_find_group_for_user, do_delete_user

# User params
user_name = "Oleg"
user_email = "oleg-test@test.com"
# Postgres db connection params
myConnection = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='postgres')


def test_tc_2(browser):

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

    # Add new user
    admin_page.add_user()
    add_user_page = AddUserPage(browser)
    add_user_page.should_be_add_user_page()
    add_user_page.create_user(user_name, "123123Aa!", "123123Aa!")
    change_user_page = ChangeUserPage(browser)
    change_user_page.should_be_change_user_page()

    # Add group for the new user
    change_user_page.add_group_for_user()
    change_user_page.add_user_email(user_email)
    change_user_page.save_new_user()

    # Find added user in DB
    do_find_user(myConnection, user_name, user_email)

    # Check that user is in the group
    do_find_group_for_user(myConnection, user_email, "First")

    # Teardown: Remove created user from table
    do_delete_user(myConnection, user_name, user_email)
    myConnection.close()
