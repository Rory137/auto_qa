import random
import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


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

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('Yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('Impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('No')
            output_no = radio_button_page.get_output_result()
            time.sleep(3)
            assert output_yes == 'Yes', "Yes have not been selected"
            assert output_impressive == 'Impressive', "Impressive have not ben selected"
            assert output_no == 'No', "No have been selected"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            time.sleep(5)
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            time.sleep(3)
            print(key_word)
            print(table_result)
            assert key_word in table_result, "the person wa not found in the table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            time.sleep(4)
            row = web_table_page.check_search_person()

            assert age in row, "the person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], "The number of rows in the table has not been changed or has changed incorrectly"
