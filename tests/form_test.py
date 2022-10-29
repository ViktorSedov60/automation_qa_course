from time import sleep

from pages.form_page import FormPage


class TestForm:
    class TestFormPage:
        # ТЕСТИРОВАНИЕ ЗАПОЛОНЕНИЯ ФОРМЫ, С ИСПОЛЬЗОВАНИЕМ ГЕНЕРАТОРА
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            per = form_page.fill_form_field()
            result = form_page.form_result()
            print(per.firstname, per.lastname, per.email)
            print(result[0], result[1])
            assert [per.firstname + " " + per.lastname, per.email] == [result[0], result[1]], 'Что то пошло не так'

