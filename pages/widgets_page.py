from time import sleep

from selenium.common import TimeoutException

from locators.widgets_locators import AccordianLocator
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianLocator()
    def check_accordian_page(self, accordian_num):

        accordian = {
                    'first':
                        {'title': self.locators.ACCORD_WHAT,
                        'content': self.locators.ACCORD_WHAT_CONTENT},
                    'second':
                        {'title': self.locators.ACCORD_WHERE,
                        'content': self.locators.ACCORD_WHERE_CONTENT},
                    'third':
                        {'title': self.locators.ACCORD_WHY,
                        'content': self.locators.ACCORD_WHY_CONTENT}

                    }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        # print(section_title.text)
        # print(section_content)

        # try:
        #     section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        #     sleep(3)
        # except TimeoutException:
        #     section_title.click()
        #     section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        #     sleep(3)
        return [section_title.text, len(section_content)]


