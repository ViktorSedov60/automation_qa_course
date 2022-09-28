

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def open(self):
        self.driver.get(self.url)


    def element_is_visible(self, locator):
        return wait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator):
        return wait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator):
        return wait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator):
        return wait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator):
        return wait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator):
        return wait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoVien();", element)