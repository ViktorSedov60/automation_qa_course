import random
from time import sleep

from locators.interactions_locators import SortableLocator, SelectableLocator
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortableLocator()

    def get_sortable_item(self, elements):
        item_list = self.element_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_item(self.locators.LIST_ITEM)
        item_list = random.sample(self.element_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.LIST_ITEM)
        # print(order_before)
        # print(order_after)
        return order_before, order_after

    def change_gride_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()

        order_before = self.get_sortable_item(self.locators.GRID_ITEM)
        item_list = random.sample(self.element_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.GRID_ITEM)
        # print(order_before)
        # print(order_after)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectableLocator()
    def click_selectable_item(self, elements):
        item_list = self.element_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text


