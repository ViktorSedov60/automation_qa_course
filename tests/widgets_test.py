from time import sleep

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabPage, ToolTipsPage


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

        def test_remove_multi(self, driver):
            widgets_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            widgets_page.open()
            widgets_page.fill_input_multi()
            count, count_after = widgets_page.remove_multi_label()
            assert count > count_after, 'the delete color are missing in the input'

        def test_fill_single(self, driver):
            widgets_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            widgets_page.open()
            # widgets_page.fill_input_single()
            color = widgets_page.fill_input_single()
            # widgets_page.chec_color_single()
            color_resalt = widgets_page.chec_color_single()
            assert color == color_resalt, 'the added color are missing in the input'


        def test_multi_delete(self, driver):
            widgets_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            widgets_page.open()
            first = widgets_page.multi_birth()
            second = widgets_page.fill_input_multi()
            third = widgets_page.multi_delete()
            assert first == third
            assert len(second) > first



    class TestDatePicker:
        def test_change_data(self, driver):
            data_picker = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            data_picker.open()
            value_date_before, value_date_after = data_picker.select_date()
            print(value_date_before, value_date_after)
            assert value_date_before != value_date_after



        def test_change_date_time(self, driver):
            data_picker = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            data_picker.open()
            value_date_before, value_date_after = data_picker.select_date_time()
            print(value_date_before, value_date_after)
            assert value_date_before != value_date_after


    class TestSlider:
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()

            print(before)
            print(after)
            assert before != after



    class  TestProgressBar:
        def test_progress_bar(self, driver):
            bar_progress = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            bar_progress.open()
            # sleep(2)
            before, after = bar_progress.change_progress_bar()
            assert before != after


    class TestTab:
        def test_tab(selfs, driver):
            tab_test = TabPage(driver, 'https://demoqa.com/tabs')
            tab_test.open()
            # driver.maximize_window()
            what, origin, use = tab_test.change_tab()
            # print(what, origin, use)
            assert what != 0
            assert origin > 0
            assert use > 0


    class TestToolTips:
        def test_tool_tips(self, driver):
            tool_tips = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips.open()
            button, field, contrary, section = tool_tips.check_tool_tip()

            assert button == 'You hovered over the Button'
            assert field == 'You hovered over the text field'
            assert contrary == 'You hovered over the Contrary'
            assert section == 'You hovered over the 1.10.32'


