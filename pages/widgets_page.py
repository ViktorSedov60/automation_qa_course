import random
from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_locators import AccordianLocator, AutoCompleteLocator, DatePickerLocator, SliderLocator, ProgressBarLocator, TabLocator
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

    def multi_birth(self):
        count_value_now = len(self.element_are_present(self.locators.MULTI_CONTAINER))
        return count_value_now



    def multi_delete(self):
        self.element_is_present(self.locators.MULTI_DELETE).click()
        count_value_after = len(self.element_are_present(self.locators.MULTI_CONTAINER))
        return count_value_after


class DatePickerPage(BasePage):
    locators = DatePickerLocator()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.DATE_TIME_MONTH).click()

        self.set_date_item_from_list(self.locators.DATE_TIME_MONTH_LIST, date.month)
        self.element_is_clickable(self.locators.DATE_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_YEAR_LIST, date.year)
        self.set_date_item_from_list(self.locators.SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after





    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)


    def set_date_item_from_list(self, elements, value):
        item_list = self.element_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break



class SliderPage(BasePage):
    locators = SliderLocator()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE)
        before = value_before.get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)

        value_after = self.element_is_visible(self.locators.SLIDER_VALUE)
        after = value_after.get_attribute('value')


        return before, after




class ProgressBarPage(BasePage):
    locators = ProgressBarLocator()

    def change_progress_bar(self):

        self.element_is_visible(self.locators.START_STOP_BUTTON).click()
        sleep(1)
        self.element_is_visible(self.locators.START_STOP_BUTTON).click()
        value_before = self.element_is_present(self.locators.PROGRESS_BAR).text

        progress_bar_button = self.element_is_visible(self.locators.START_STOP_BUTTON)
        progress_bar_button.click()
        sleep(random.randint(1, 5))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR).text
        return value_before, value_after


class TabPage(BasePage):
    locators = TabLocator()
    def change_tab(self):
        # self.remove_footer()
        # self.driver.maximize_window()
        self.element_is_visible(self.locators.WHAT_TAB).click()
        what_tab = self.element_is_visible(self.locators.WHAT_TEXT).text
        self.element_is_visible(self.locators.ORIGIN_TAB).click()
        origin_tab = self.element_is_visible(self.locators.ORIGIN_TEXT).text
        self.element_is_visible(self.locators.USE_TAB).click()
        use_tab = self.element_is_visible(self.locators.USE_TEXT).text
        # self.element_is_visible(self.locators.MORE_TAB).click()
        # more_tab = self.element_is_visible(self.locators.MORE_TEXT).text
        return len(what_tab), len(origin_tab), len(use_tab)  # len(more_tab)




