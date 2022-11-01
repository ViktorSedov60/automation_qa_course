from time import sleep

from pages.widgets_page import AccordianPage, AutoCompletePage


class TestWidgets:
    class TestAccordian:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            driver.maximize_window() # Пришлось увеличить размер окна из-за закрытия места клика
            first_title, first_content = accordian_page.check_accordian_page('first')
            second_title, second_content =  accordian_page.check_accordian_page('second')
            third_title, third_content = accordian_page.check_accordian_page('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'incorrect title missing test'
            assert second_title == 'Where does it come from?' and second_content > 0, 'incorrect title missing test'
            assert third_title == 'Why do we use it?' and third_content > 0, 'incorrect title missing test'


    class TestAutoComplete:
        def test_auto_complete(self,driver):
            widgets_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            widgets_page.open()
            colors = widgets_page.fill_input_multi()
            colors_result = widgets_page.chek_color_multi()
            assert colors == colors_result, 'the added colors are missing in the input'

        def test_remove_multi(selfs, driver):
            widgets_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            widgets_page.open()
            widgets_page.fill_input_multi()
            count, count_after = widgets_page.remove_multi_label()
            assert count > count_after, 'the added colors are missing in the input'

        def test_fill_single(self, driver):
            widgets_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            widgets_page.open()
            # widgets_page.fill_input_single()
            color = widgets_page.fill_input_single()
            # widgets_page.chec_color_single()
            color_resalt = widgets_page.chec_color_single()
            assert color == color_resalt, 'the added colors are missing in the input'


