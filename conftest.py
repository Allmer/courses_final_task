from selenium import webdriver
import pytest
from helpers.db_query import DB
from helpers.testdata import CreateBDGroup, CreateUserAndAddGroup


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(
        executable_path="/usr/local/bin/chromedriver",
        options=options
    )

    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def add_bd_group_and_delete_group():
    # Create DB connection
    db = DB()
    # Creating group in DB table
    db.do_insert_group(CreateBDGroup.group_name_tcbg)
    yield
    # Browser test
    # Teardown: delete group in DB table
    db.do_delete_group(CreateBDGroup.group_name_tcbg)
    # Close cursor and connection
    db.close_cursor()


@pytest.fixture
def create_user_add_group_check_usergroup():
    # Create DB connection
    db = DB()
    yield
    db.do_find_user(
        CreateUserAndAddGroup.user_name,
        CreateUserAndAddGroup.user_email
    )
    db.do_find_group_for_user(
        CreateUserAndAddGroup.user_email,
        CreateUserAndAddGroup.group_name_tcuaag
    )
    db.do_delete_user(
        CreateUserAndAddGroup.user_name,
        CreateUserAndAddGroup.user_email
    )
    db.close_cursor()
