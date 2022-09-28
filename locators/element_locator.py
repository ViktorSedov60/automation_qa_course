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



