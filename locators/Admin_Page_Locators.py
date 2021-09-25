from selenium.webdriver.common.by import By


class AdminPageLocators:

    LOCATOR_ADMIN_PAGE_HEADER = (By.XPATH, "//div[@id='content']/h1")
    LOCATOR_GROUP_LINK = (By.XPATH, "//tr[@class='model-group']/th/a")
    LOCATOR_ADD_USER_BUTTON = (By.XPATH, "//div[@id='content-main']/div[2]/table/tbody/tr[2]/td/a")
