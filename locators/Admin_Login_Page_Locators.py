from selenium.webdriver.common.by import By


class AdminLoginPageLocators:

    LOCATOR_FORM_HEADER = (By.XPATH, "//h1[@id='site-name']/a")
    LOCATOR_FORM_USERNAME = (By.XPATH, "//input[@id='id_username']")
    LOCATOR_FORM_PASSWORD = (By.XPATH, "//input[@id='id_password']")
    LOCATOR_FORM_SUBMIT = (By.XPATH, "//div[@class='submit-row']/input")
