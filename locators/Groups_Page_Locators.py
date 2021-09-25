from selenium.webdriver.common.by import By


class GroupsPageLocators:

    LOCATOR_GROUPS_PAGE_HEADER = (By.XPATH, "//div[@id='content']/h1")
    LOCATOR_GROUPS_PAGE_SEARCH = (By.XPATH, "//form[@id='changelist-search']/div/input[1]")
    LOCATOR_GROUPS_PAGE_SEARCH_SUBMIT = (By.XPATH, "//form[@id='changelist-search']/div/input[2]")
    LOCATOR_GROUPS_PAGE_RESULT = (By.XPATH, "//table[@id='result_list']/tbody/tr/th/a")
