from pages.base_page import BasePage
from locators.Groups_Page_Locators import GroupsPageLocators


class GroupsPage(BasePage):

    def should_be_groups_page(self):
        groups_page_header_text = self.find_element(
            GroupsPageLocators.LOCATOR_GROUPS_PAGE_HEADER).text
        assert groups_page_header_text == "Select group to change",\
            f"Select group to change not eq {groups_page_header_text}"

    def search_for_group(self, search_phrase: str):
        search_field = self.find_element(
            GroupsPageLocators.LOCATOR_GROUPS_PAGE_SEARCH)
        search_field.send_keys(search_phrase)
        search_button = self.find_element(
            GroupsPageLocators.LOCATOR_GROUPS_PAGE_SEARCH_SUBMIT)
        search_button.click()

    def check_search_results(self, created_group):
        search_result = self.find_element(
            GroupsPageLocators.LOCATOR_GROUPS_PAGE_RESULT).text
        assert search_result == created_group,\
            f"created_group not eq {search_result}"
