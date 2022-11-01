import random
from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_locators import AccordianLocator, AutoCompleteLocator
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

class AutoCompletePage(BasePage):
    locators = AutoCompleteLocator()

    def fill_input_multi(self):
        # color = next(generated_color()).color_name
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_multi_label(self):
        count_value_list = len(self.element_are_present(self.locators.MULTI_LABEL))
        remove_button_list = self.element_are_present(self.locators.MALTI_LABEL_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.element_are_present(self.locators.MULTI_LABEL))
        return count_value_list, count_value_after

    def chek_color_multi(self):
        color_list = self.element_are_present(self.locators.MULTI_LABEL)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGL_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def chec_color_single(self):
        color = self.element_is_visible(self.locators.SINGL_CONTAINER)
        return color.text

    def multi_now(self):
        count_value_now = len(self.element_are_present(self.locators.MULTI_CONTAINER))
        return count_value_now



    def multi_delete(self):
        self.element_is_present(self.locators.MULTI_DELETE).click()
        count_value_after = len(self.element_are_present(self.locators.MULTI_CONTAINER))
        return count_value_after


