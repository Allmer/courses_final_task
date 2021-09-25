from selenium.webdriver.common.by import By


class ChangeUserPageLocators:

    LOCATOR_CHANGE_USER_PAGE_HEADER = (By.XPATH, "//div[@id='content']/h1")
    LOCATOR_FIRST_GROUP = (By.XPATH, "//div[@class='selector-available']/select/option[@title='First']")
    LOCATOR_CHOOSE_GROUP = (By.XPATH, "//div[@class='selector']/ul/li[1]/a")
    LOCATOR_EMAIL_FIELD = (By.XPATH, "//input[@id='id_email']")
    LOCATORS_SAVE_BUTTON = (By.XPATH, "//div[@class='submit-row']")
