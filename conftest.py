from selenium import webdriver
import pytest
from helpers.db_client import DB
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
def delete_group():
    # Create DB connection
    db = DB()

    yield
    # Browser test
    # Teardown: delete group in DB table
    db.do_delete_group(CreateBDGroup.group_name_tcbg)
    # Close cursor and connection
    db.close_cursor()


@pytest.fixture
def delete_user():

    db = DB()
    yield

    db.do_delete_user(
        CreateUserAndAddGroup.user_name,
        CreateUserAndAddGroup.user_email
    )
    db.close_cursor()
