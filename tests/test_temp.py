from pages.main_page import MainPage


def test_tc_1(browser, add_bd_group_and_delete_group):

    # Здесь то что должна делать фикстура:
    # Add group to db table
    #DB.do_insert_group(myConnection, created_group)

    # Это типа тест в браузере
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.should_be_main_page()

    # Здесь то что должна делать фикстура:
    # Teardown: Remove created group from table
    #DB.do_delete_group(myConnection)

