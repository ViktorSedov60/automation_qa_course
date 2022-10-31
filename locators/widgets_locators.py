from selenium.webdriver.common.by import By


class AccordianLocator:
    ACCORD_WHAT = (By.CSS_SELECTOR, 'div#section1Heading')
    ACCORD_WHAT_CONTENT = (By.CSS_SELECTOR, 'div#section1Content p')
    ACCORD_WHERE = (By.CSS_SELECTOR, 'div#section2Heading')
    ACCORD_WHERE_CONTENT = (By.CSS_SELECTOR, 'div#section2Content p')
    ACCORD_WHY = (By.CSS_SELECTOR, 'div#section3Heading')
    ACCORD_WHY_CONTENT = (By.CSS_SELECTOR, 'div#section3Content p')


