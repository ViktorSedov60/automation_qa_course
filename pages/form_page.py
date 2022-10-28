
import os
from selenium.webdriver import Keys
from generator.generator import generator_person, generated_file
from locators.form_locators import FormLocators
from pages.base_page import BasePage


class FormPage(BasePage):

    locators = FormLocators()
    def fill_form_field(self):
        person = next(generator_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECT).send_keys('English')
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_visible(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.go_to_element(self.element_is_present(self.locators.SELECT_STATE))
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.element_are_visible(self.locators.RESALT_TABLE)
        # data = []
        data = [i.text for i in result_list]
        # for item in result_list:
        #     data.append(item.text)
        return data
