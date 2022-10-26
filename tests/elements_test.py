import random
from time import sleep

from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, UpLoadAndDownLoad


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
            assert key_word in table_result, 'the person was not found in the table'

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            print(age)
            print(row)
            assert age in row, 'the person card has been changed'

        def test_web_table_delite_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_delete()
            print(text)
            assert text == 'No rows found'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], 'Нет доступа к страницам'


    class TestButtonsPage:
        def test_different_click_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            print(double)
            print(right)
            print(click)
            assert double == "You have done a double click", "The double click button not pressed"
            assert right == "You have done a right click", "The right click button not pressed"
            assert click == "You have done a dynamic click", "The dynamic click button not pressed"



    class TestLinksPage:

        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, result = links_page.check_new_tab_simple_link()

            assert href_link == result


        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            print(response_code)
            assert response_code == 400


    class TestUpLoadAndDownLoad:

        def test_upload_file(selfs, driver):
            upload_page = UpLoadAndDownLoad(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            file_name, result = upload_page.upload_file()
            assert file_name == result, "the file has not been upload"


        def test_download_file(self,driver):
            download_page = UpLoadAndDownLoad(driver, 'https://demoqa.com/upload-download')
            download_page.open()
            check = download_page.download_files()
            assert check is True, "the file has not been udownload"

