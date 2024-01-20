import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage


# def test(driver):
#     page = BasePage(driver,"https://www.google.com")
#     page.open()
#     time.sleep(3)


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            time.sleep(5)
            output_name, output_email,output_current_addres, output_per_adrres = text_box_page.check_fields_form()

            assert full_name == output_name, "the full name does not mach"
            assert email == output_email, "the email does not mach"
            assert current_address == output_current_addres, "the current address does not mach"
            assert permanent_address == output_per_adrres, "the permanent address does not mach"

    class TestCheckBox:

        def test_check_box(self,driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            time.sleep(5)
            check_box_page.click_random_checkbox()
            time.sleep(10)
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "checkboxes have not been selected"