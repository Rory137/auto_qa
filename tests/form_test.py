from pages.form_page import FormPage
import time

class TestForm:
    class TestFormPage:
        def test_form(self,driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person_info = form_page.fill_form_fields()
            time.sleep(5)
            result = form_page.form_result()
            print(person_info.firstname, person_info. lastname, person_info.email)
            print(result[0], result[1])
            assert [person_info.firstname + " " + person_info. lastname, person_info.email] == [result[0], result[1]]
