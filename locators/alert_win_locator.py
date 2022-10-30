from selenium.webdriver.common.by import By


class AlertTabWinLocator:
    TAB_BUTTON = (By.CSS_SELECTOR, 'button#tabButton')
    WIN_BUTTON = (By.CSS_SELECTOR, 'button#windowButton')
    MESS_BUTTON = (By.CSS_SELECTOR, 'button#messageWindowButton')


    TAB_NEW = (By.CSS_SELECTOR, 'h1#sampleHeading')

    WIN_NEW = (By.CSS_SELECTOR, 'body')

class AlertPageLocator:
    ALERT_BUTTON1 = (By.CSS_SELECTOR, 'button#alertButton')
    ALERT_BUTTON2 = (By.CSS_SELECTOR, 'button#timerAlertButton')
    ALERT_BUTTON3 = (By.CSS_SELECTOR, 'button#confirmButton')
    ALERT_BUTTON3_RESULT = (By.CSS_SELECTOR, 'span#confirmResult')
    ALERT_BUTTON4 = (By.CSS_SELECTOR, 'button#promtButton')
    ALERT_BUTTON4_RESULT = (By.CSS_SELECTOR, 'span#promptResult')

class FramePageLocator:
    FRAME1 = (By.CSS_SELECTOR, 'iframe#frame1')
    FRAME2 = (By.CSS_SELECTOR, 'iframe#frame2')
    TITLE_FRAME = (By.CSS_SELECTOR, 'h1#sampleHeading')


