from time import sleep

from pages.element_page import TextBoxPage


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


            sleep(5)
