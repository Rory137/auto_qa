import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage


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

