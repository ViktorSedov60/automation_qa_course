import random
from time import sleep

from locators.interactions_locators import SortableLocator, SelectableLocator, ResizableLocator, DroppableLocator
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

class ResizablePage(BasePage):
    locators = ResizableLocator()

    def get_pixels(self, size_value):
        wight = size_value.split(';')[0].split(':')[1].replace(' ', '')
        height = size_value.split(';')[1].split(':')[1].replace(' ', '')

        return wight, height


    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')

        return size_value

    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 50, 60)
        max_box = self.get_pixels(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -100, -90)
        min_box = self.get_pixels(self.get_max_min_size(self.locators.RESIZABLE_BOX))

        return max_box, min_box

    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE), 50, 60)
        max_size = self.get_pixels(self.get_max_min_size(self.locators.RESIZABLE))
        # sleep(2)
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE), -30, -40)
        min_size = self.get_pixels(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppableLocator()
    def drop_simpl(self):
        drag_div = self.element_is_visible(self.locators.DRAG_ME)
        drop_div = self.element_is_visible(self.locators.DROP_HERE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def not_acceptable(self):
        self.element_is_visible(self.locators.ACCEPT).click()
        # sleep(2)
        not_accept = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        not_accept_after = self.element_is_visible(self.locators.DROP_HERE_ACCERT)
        self.action_drag_and_drop_to_element(not_accept, not_accept_after)
        return not_accept_after.text

    def acceptable(self):
        acceptable = self.element_is_visible(self.locators.ACCEPTABLE)
        accept_after = self.element_is_visible(self.locators.DROP_HERE_ACCERT)
        self.action_drag_and_drop_to_element(acceptable, accept_after)
        return accept_after.text

    def prevent_propogation(self):
        self.element_is_visible(self.locators.PREVENT_PROPOGATION).click()
        drag_mi = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        outer_droppable = self.element_is_visible(self.locators.OUTER_DROPPABLE)
        inner_droppable = self.element_is_visible(self.locators.INNER_DROPPABLE)
        self.action_drag_and_drop_to_element(drag_mi, inner_droppable)
        return outer_droppable.text, inner_droppable.text

    def prevent(self):
        self.element_is_visible(self.locators.PREVENT_PROPOGATION).click()
        drag_mi = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        outer_droppable_greedy = self.element_is_visible(self.locators.OUTER_DROPPABLE_GREEDY)
        inner_droppable_greedy = self.element_is_visible(self.locators.INNER_DROPPABLE_GREEDY)
        self.action_drag_and_drop_to_element(drag_mi, inner_droppable_greedy)
        sleep(5)
        # outer_after =  self.element_is_visible(self.locators.OUTER_DROPPABLE_GREEDY)
        # self.action_drag_and_drop_to_element(drag_mi, outer_after)
        return outer_droppable_greedy.text, inner_droppable_greedy.text #, outer_after.text

    def revert_revert_draggable(self, type_drag):
        drags = {
            'will':
                {'revert': self.locators.WILL_REVERT, },
            'not_will':
                {'revert': self.locators.NOT_REVERT,},
                 }
        self.element_is_visible(self.locators.REVERT_DRAGGABLE).click()
        revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_revert = revert.get_attribute('style')
        sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_revert, position_after_revert












