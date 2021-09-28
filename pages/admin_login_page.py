from pages.base_page import BasePage
from locators.Admin_Login_Page_Locators import AdminLoginPageLocators


class AdminLoginPage(BasePage):

    def should_be_admin_login_page(self):
        form_header_text = self.find_element(
            AdminLoginPageLocators.LOCATOR_FORM_HEADER).text
        assert form_header_text == "Django administration",\
            f"Django administration not eq {form_header_text}"

    def login_to_admin_account(self, username: str, password: str):
        username_field = self.find_element(AdminLoginPageLocators.LOCATOR_FORM_USERNAME)
        username_field.send_keys(username)
        password_field = self.find_element(AdminLoginPageLocators.LOCATOR_FORM_PASSWORD)
        password_field.send_keys(password)
        log_in_button = self.find_element(AdminLoginPageLocators.LOCATOR_FORM_SUBMIT)
        log_in_button.click()
