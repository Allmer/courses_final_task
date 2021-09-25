from pages.base_page import BasePage
from locators.Admin_Page_Locators import AdminPageLocators


class AdminPage(BasePage):

    def should_be_admin_page(self):
        admin_page_header = self.find_element(
            AdminPageLocators.LOCATOR_ADMIN_PAGE_HEADER).text
        assert admin_page_header == "Site administration"

    def open_groups_page(self):
        self.find_element(AdminPageLocators.LOCATOR_GROUP_LINK).click()

    def add_user(self):
        self.find_element(AdminPageLocators.LOCATOR_ADD_USER_BUTTON).click()
