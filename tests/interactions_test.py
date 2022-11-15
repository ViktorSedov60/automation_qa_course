from pages.interactions_page import SortablePage, SelectablePage


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
