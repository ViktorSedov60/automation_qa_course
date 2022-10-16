from selenium.webdriver.common.by import By


# FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
# LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
# EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
# GENDER = (By.CSS_SELECTOR, f'label[for ="gender-radio-{randint(1 ,3)}"]')
# MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')
# SUBJECT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
# HOBBIES = (By.CSS_SELECTOR, f'label[for ="hobbies-checkbox-{randint(1 ,3)}"]')
# FILE_INPUT = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
# CURRENT_ADDRESS = (By.CSS_SELECTOR, 'input[id="currentAddress"]')
# SUBMIT = (By.CSS_SELECTOR, 'input[id="submit"]')


class TextBoxLocator:
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button.btn')

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'p#currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')

    # CHECKED_ITEMS = 'svg[class="rct-icon rct-icon-check"]'
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')

    # TITLE_ITEMS = ".//ancestor::span[@class='rct-text']"
    TITLE_ITEMS = ".//ancestor::label[@*]"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESS_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")

    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

