from pages.interactions_page import SortablePage

class TestInteractions:

    class TestSortable:
        def test_sortable(self, driver):
            sortable_test = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_test.open()
            list_before, list_after = sortable_test.change_list_order()
            grid_before, grid_after = sortable_test.change_gride_order()
            assert  list_before != list_after
            assert grid_before != grid_after