from pages.widgets_page import AccordianPage


class TestWidgest:
    class TestAccordian:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            driver.maximize_window()
            first_title, first_content = accordian_page.check_accordian_page('first')
            second_title, second_content =  accordian_page.check_accordian_page('second')
            third_title, third_content = accordian_page.check_accordian_page('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0

