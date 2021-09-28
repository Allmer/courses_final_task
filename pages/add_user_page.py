from pages.base_page import BasePage
from locators.Add_User_Page_Locators import AddUserPageLocators


class AddUserPage(BasePage):

    def should_be_add_user_page(self):
        add_user_page_header = self.find_element(
            AddUserPageLocators.LOCATOR_ADD_USER_PAGE_HEADER).text
        assert add_user_page_header == "Add user",\
            f"Add user not eq {add_user_page_header}"

    def create_user(self, username: str, password: str, password_confirmation: str):
        username_field = self.find_element(
            AddUserPageLocators.LOCATOR_ADD_USER_PAGE_USERNAME)
        username_field.send_keys(username)
        password_field = self.find_element(
            AddUserPageLocators.LOCATOR_ADD_USER_PAGE_PASSWORD)
        password_field.send_keys(password)
        password_confirmation_field = self.find_element(
            AddUserPageLocators.LOCATOR_ADD_USER_PAGE_C_PASSWORD)
        password_confirmation_field.send_keys(password_confirmation)
        save_button = self.find_element(
            AddUserPageLocators.LOCATOR_ADD_USER_PAGE_SAVE)
        save_button.click()
