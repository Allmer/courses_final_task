from selenium import webdriver
import pytest
from helpers.db_query import DB


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def add_bd_group_and_delete_group():
    # Create DB connection
    db = DB()
    # Creating group in DB table
    db.do_insert_group("Third")
    yield
    # Browser test
    # Teardown: delete group in DB table
    db.do_delete_group("Third")
    # Close cursor and connection
    db.close_cursor()


@pytest.fixture
def create_user_add_group_check_usergroup():
    # Create DB connection
    db = DB()
    yield
    db.do_find_user(username, email)
    db.do_find_group_for_user(email, group_name)
    db.do_delete_user(username, email)
    db.close_cursor()
    