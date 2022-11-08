from selenium.webdriver.common.by import By


class AccordianLocator:
    ACCORD_WHAT = (By.CSS_SELECTOR, 'div#section1Heading')
    ACCORD_WHAT_CONTENT = (By.CSS_SELECTOR, 'div#section1Content p')
    ACCORD_WHERE = (By.CSS_SELECTOR, 'div#section2Heading')
    ACCORD_WHERE_CONTENT = (By.CSS_SELECTOR, 'div#section2Content p')
    ACCORD_WHY = (By.CSS_SELECTOR, 'div#section3Heading')
    ACCORD_WHY_CONTENT = (By.CSS_SELECTOR, 'div#section3Content p')

class AutoCompleteLocator:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input#autoCompleteMultipleInput')
    MULTI_LABEL = (By.CSS_SELECTOR, 'div.css-12jo7m5')
    MALTI_LABEL_REMOVE = (By.CSS_SELECTOR, 'div.css-xb97g8 svg path')
    # MALTI_LABEL_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    MULTI_DELETE = (By.CSS_SELECTOR, 'div.auto-complete__clear-indicator svg path')
    MULTI_CONTAINER = (By.CSS_SELECTOR, 'div#autoCompleteMultipleContainer')


    SINGL_INPUT = (By.CSS_SELECTOR, 'input#autoCompleteSingleInput')
    SINGL_CONTAINER = (By.CSS_SELECTOR, 'div.auto-complete__single-value')



class DatePickerLocator:
    DATE_INPUT = (By.CSS_SELECTOR, 'input#datePickerMonthYearInput')
    SELECT_MONTH = (By.CSS_SELECTOR, 'select.react-datepicker__month-select')
    SELECT_YEAR = (By.CSS_SELECTOR, 'select.react-datepicker__year-select')
    SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__day.react-datepicker__day')

    DATE_TIME_INPUT = (By.CSS_SELECTOR, 'input#dateAndTimePickerInput')
    DATE_TIME_MONTH = (By.CSS_SELECTOR, 'div.react-datepicker__month-read-view')
    DATE_TIME_YEAR = (By.CSS_SELECTOR, 'div.react-datepicker__year-read-view')
    DATE_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li.react-datepicker__time-list-item ')
    DATE_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__month-option')
    DATE_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__year-dropdown')

