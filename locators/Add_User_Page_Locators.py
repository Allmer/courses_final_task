from selenium.webdriver.common.by import By


class AddUserPageLocators:

    LOCATOR_ADD_USER_PAGE_HEADER = (By.XPATH, "//div[@id='content']/h1")
    LOCATOR_ADD_USER_PAGE_USERNAME = (By.XPATH, "//input[@id='id_username']")
    LOCATOR_ADD_USER_PAGE_PASSWORD = (By.XPATH, "//input[@id='id_password1']")
    LOCATOR_ADD_USER_PAGE_C_PASSWORD = (By.XPATH, "//input[@id='id_password2']")
    LOCATOR_ADD_USER_PAGE_SAVE = (By.XPATH, "//input[@name='_save']")
