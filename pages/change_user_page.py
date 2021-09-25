from pages.base_page import BasePage
from locators.Change_User_Page_Locators import ChangeUserPageLocators


class ChangeUserPage(BasePage):

    def should_be_change_user_page(self):
        change_user_page_header = self.find_element(
            ChangeUserPageLocators.LOCATOR_CHANGE_USER_PAGE_HEADER).text
        assert change_user_page_header == "Change user"

    def add_group_for_user(self):
        choose_group_in_selector = self.find_element(
            ChangeUserPageLocators.LOCATOR_FIRST_GROUP)
        choose_group_in_selector.click()
        choose_button = self.find_element(
            ChangeUserPageLocators.LOCATOR_CHOOSE_GROUP)
        choose_button.click()

    def add_user_email(self, email: str):
        email_field = self.find_element(
            ChangeUserPageLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)

    def save_new_user(self):
        save_button = self.find_element(
            ChangeUserPageLocators.LOCATORS_SAVE_BUTTON)
        save_button.click()
