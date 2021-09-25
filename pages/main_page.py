from pages.base_page import BasePage
from locators.Main_Page_Locators import MainPageLocators


class MainPage(BasePage):

    def should_be_main_page(self):
        header_text = self.find_element(
            MainPageLocators.LOCATOR_MAIN_PAGE_H1).text
        assert header_text == "Simple Django Application"

    def open_admin_page(self):
        self.find_element(MainPageLocators.LOCATOR_ADMIN_BUTTON).click()


