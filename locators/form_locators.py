import random

from selenium.webdriver.common.by import By


class FormLocators:
    FIRST_NAME = (By.CSS_SELECTOR, 'input#firstName')
    LAST_NAME = (By.CSS_SELECTOR, 'input#lastName')
    EMAIL = (By.CSS_SELECTOR, 'input#userEmail')
    GENDER = (By.CSS_SELECTOR, f'label[for="gender-radio-{random.randint(1,3)}"]')
    MOBILE = (By.CSS_SELECTOR, 'input#userNumber')
    # DATE_OF_BIRTH = (By.CSS_SELECTOR, '')
    SUBJECT = (By.CSS_SELECTOR, 'input#subjectsInput')
    HOBBIES = (By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{random.randint(1,3)}"]')
    FILE_INPUT = (By.CSS_SELECTOR, 'input#uploadPicture')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea#currentAddress')
    SELECT_STATE = (By.CSS_SELECTOR, 'div#state')
    STATE_INPUT = (By.CSS_SELECTOR, 'input#react-select-3-input')
    SELECT_CITY = (By.CSS_SELECTOR, 'div#city')
    CITY_INPUT = (By.CSS_SELECTOR, 'input#react-select-4-input')
    SUBMIT = (By.CSS_SELECTOR, 'button.btn')

    # TABLE RESALT

    RESALT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
