from time import sleep

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


class TestInteractions:

    class TestSortable:
        def test_sortable(self, driver):
            sortable_test = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_test.open()
            list_before, list_after = sortable_test.change_list_order()
            grid_before, grid_after = sortable_test.change_gride_order()
            assert list_before != list_after
            assert grid_before != grid_after

    class TestSelectable:
        def test_selectable(self, driver):
            selectable_test = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_test.open()
            item_list = selectable_test.select_list_item()
            item_grid = selectable_test.select_grid_item()
            assert len(item_list) > 0, 'no element were selected'
            assert len(item_grid) > 0, 'no element were selected'


    class TestResizable:
        def test_resizable(self,driver):
            resizable_test = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_test.open()
            max_box, min_box = resizable_test.change_size_resizable_box()
            # sleep(3)
            max_resize, min_resize = resizable_test.change_size_resizable()

            assert max_box != min_box
            assert max_resize != min_resize



    class TestDrooable:
        def test_simple(self, driver):
            droppable_test = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_test.open()
            text = droppable_test.drop_simpl()
            text_not_accept = droppable_test.not_acceptable()
            text_accept = droppable_test.acceptable()
            assert text == 'Dropped!'
            assert text_not_accept != 'Dropped!'
            assert text_accept == 'Dropped!'


        def test_revent(self, driver):
            droppable_test = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_test.open()
            text_outer, text_inner = droppable_test.prevent_propogation()
            text_outer_greedy, text_inner_greedy= droppable_test.prevent()
            assert text_outer == 'Dropped!'
            assert text_inner == 'Dropped!'
            assert text_outer_greedy != 'Dropped!'
            assert text_inner_greedy == 'Dropped!'

        def test_will_revert(self, driver):
            droppable_test = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_test.open()
            will, will_after = droppable_test.revert_revert_draggable('will')
            not_will, not_will_after = droppable_test.revert_revert_draggable('not_will')
            assert will != will_after
            assert not_will ==not_will_after



