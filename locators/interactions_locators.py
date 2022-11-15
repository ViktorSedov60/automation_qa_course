from selenium.webdriver.common.by import By


class SortableLocator:
    TAB_LIST = (By.CSS_SELECTOR, 'a#demo-tab-list')
    LIST_ITEM = (By.CSS_SELECTOR, 'div#demo-tabpane-list div.list-group-item')
    TAB_GRID = (By.CSS_SELECTOR, 'a#demo-tab-grid')
    GRID_ITEM = (By.CSS_SELECTOR, 'div#demo-tabpane-grid div.list-group-item')


class SelectableLocator:
    LIST_TAB = (By.CSS_SELECTOR, 'a#demo-tab-list')
    LIST_ITEM = (By.CSS_SELECTOR, 'ul#verticalListContainer li')
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, 'ul#verticalListContainer li.active')

    GRID_TAB = (By.CSS_SELECTOR, 'a#demo-tab-grid')
    GRID_ITEM = (By.CSS_SELECTOR, 'div#gridContainer li')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'div#gridContainer li.active')

