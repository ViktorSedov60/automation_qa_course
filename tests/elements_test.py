import random
from time import sleep

from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            # input_data = text_box_page.fill_all_fields()
            # output_data = text_box_page.check_filled_form()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            # print(f'\n{input_data}')
            print(f'\n{output_name}')
            # print(output_data)
            print(output_email),
            print(output_cur_addr)
            print(output_per_addr)

            assert full_name == output_name, "not full_name"
            assert email == output_email, "not email"
            assert current_address == output_cur_addr, "not current_address"
            assert permanent_address == output_per_addr, "not permanent_address"
            # assert input_data == output_data, "что то пошло не так"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_result = check_box_page.get_checkbox()
            output_result = check_box_page.get_output_result()
            print(input_result)
            print(output_result)
            assert input_result == output_result, 'checkboxes have not been selected'



    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()

            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            sleep(5)

            radio_button_page.click_on_the_radio_button('impres')
            output_impressive = radio_button_page.get_output_result()
            sleep(5)

            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            sleep(5)

            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Yes' have not been selected"
            assert output_no == 'No', "'Yes' have not been selected"


    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_resalt = web_table_page.check_new_added_person()
            print(new_person)
            print(table_resalt)
            assert new_person in table_resalt


        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            print(key_word)
            print(table_result)
            assert key_word in table_result

