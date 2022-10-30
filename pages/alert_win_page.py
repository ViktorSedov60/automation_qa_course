import random
from time import sleep

from locators.alert_win_locator import AlertTabWinLocator, AlertPageLocator, FramePageLocator, NestedFreameLocator, ModalDialogsLocator
from pages.base_page import BasePage


class NewTabPage(BasePage):
    locators = AlertTabWinLocator()
    def check_open_new_tab(self):
        self.element_is_visible(self.locators.TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TAB_NEW).text

        return text_title

    def check_open_new_win(self):
        self.element_is_visible(self.locators.WIN_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TAB_NEW).text

        return text_title

    def check_open_new_mess(self):
        self.element_is_visible(self.locators.MESS_BUTTON).click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.fullscreen_window()

        text_title = self.element_is_present(self.locators.WIN_NEW).text
        # print(text_title)
        return text_title

class AlertPage(BasePage):
    locators = AlertPageLocator()

    def check_alert1(self):
        self.element_is_visible(self.locators.ALERT_BUTTON1).click()
        alert_window = self.driver.switch_to.alert
        # print(aleret_window.text)
        return alert_window.text

    def check_alert2(self):
        self.element_is_visible(self.locators.ALERT_BUTTON2).click()
        sleep(7)
        alert_window = self.driver.switch_to.alert
        # print(alert_window.text)
        return alert_window.text

    def check_alert3(self):
        self.element_is_visible(self.locators.ALERT_BUTTON3).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_visible(self.locators.ALERT_BUTTON3_RESULT).text
        # print(text_result)
        return text_result


    def check_alert4(self):
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.ALERT_BUTTON4).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_visible(self.locators.ALERT_BUTTON4_RESULT).text
        # print(text_result)
        return text, text_result

class FramePage(BasePage):
    locators = FramePageLocator()
    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FRAME1)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.FRAME2)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            return [text, width, height]

class NestedFreamePage(BasePage):
    locators = NestedFreameLocator()
    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.FRAME1)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text


        child_frame = self.element_is_present(self.locators.FRAME2)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text



        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsLocator()

    def Check_Small_Modal(self):
        small_modal = self.element_is_visible(self.locators.SMALL_MODAL).click()
        self.driver.switch_to.frame(small_modal)
        small_text = self.element_is_present(self.locators.TEXT_SMALL_MODAL).text
        small_close = self.element_is_visible(self.locators.CLOSE_SMALL_MODAL).click()
        return  small_text

    def Check_Large_Modal(self):
        large_modal = self.element_is_visible(self.locators.LARGE_MODAL).click()
        self.driver.switch_to.frame(large_modal)
        large_text = self.element_is_present(self.locators.TEXT_LARGE_MODAL).text
        large_close = self.element_is_visible(self.locators.CLOSE_LARGE_MODAL).click()
        return large_text

