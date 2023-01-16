import pytest
import allure

from page_objects.registration_form import RegistrationForm

@pytest.mark.usefixtures('setup')
class TestRegistrationForm():


    @allure.story('Успешная регистрация с вводом валидных данных')
    def test_registration_positive(self):
        registration_form = RegistrationForm(self.driver)
        try_for_free = registration_form.get_try_for_free_button()
        with allure.step("Кликаем на кнопку try for free"):
            try_for_free.click()
        with allure.step("Проверяем текст кнопки try for free"):
            assert try_for_free.text == 'try for free'
        with allure.step("Вводим валидное имя пользователя"):
            registration_form.get_username_field().send_keys('username')
        with allure.step("Вводим валидное название компании"):
            registration_form.get_company_name_field().send_keys('company_name')
        with allure.step("Вводим валидный номер телефона"):
            registration_form.get_phone_number_field().send_keys('+7 00000000')
        with allure.step("Вводим валидный email"):
            registration_form.get_email_field().send_keys('testmail@gmail.com')
        with allure.step("Кликаем на кнопку send request"):
            registration_form.get_send_request_button().click()


    @allure.story('Неуспешная регистрация с вводом невалидного email (email без @gmail.com)')
    def test_registration_bad_email(self):
        registration_form = RegistrationForm(self.driver)
        with allure.step("Кликаем на кнопку try for free"):
            registration_form.get_try_for_free_button().click()
        with allure.step("Проверяем что после нажатия на кнопку try for free изменился url"):
            assert registration_form.get_url() == 'https://nomia.net/#contact-form'
        with allure.step("Вводим валидное имя пользователя"):
            registration_form.get_username_field().send_keys('username')
        with allure.step("Вводим валидное название компании"):
            registration_form.get_company_name_field().send_keys('company_name')
        with allure.step("Вводим валидный номер телефона"):  
            registration_form.get_phone_number_field().send_keys('+7 00000000')
        with allure.step("Вводим невалидный email (без @gmail.com)"):
            registration_form.get_email_field().send_keys('testbadmail')
        with allure.step("Кликаем на кнопку send request"):    
            registration_form.get_send_request_button().click()
        with allure.step("Проверяем что после нажатия на кнопку url не сменился из за неправильного email"):
            assert registration_form.get_url() == 'https://nomia.net/#contact-form'

    
    @allure.story('Неуспешная регистрация при деактивации чек- бокса с соглашением на политику компании ')
    def test_registration_bad_checkbox(self):
        registration_form = RegistrationForm(self.driver)
        with allure.step("Кликаем на кнопку try for free"):
            registration_form.get_try_for_free_button().click()
        with allure.step("Проверяем что после нажатия на кнопку try for free изменился url"):
            assert registration_form.get_url() == 'https://nomia.net/#contact-form'
        with allure.step("Вводим валидное имя пользователя"):
            registration_form.get_username_field().send_keys('username')
        with allure.step("Вводим валидное название компании"):
            registration_form.get_company_name_field().send_keys('company_name')
        with allure.step("Вводим валидный номер телефона"):  
            registration_form.get_phone_number_field().send_keys('+7 00000000')
        with allure.step("Вводим валидный email"):
            registration_form.get_email_field().send_keys('testmail@gmail.com')
        with allure.step("Кликаем на чек- бокс для его деактивации"):
            registration_form.get_agreement_button().click()
        with allure.step("Проверяем что чек- бокс стал неактивным"):
            assert registration_form.get_agreement_button().is_selected() == False
        with allure.step("Проверяем что кнопка send request стала disabled"):
            assert registration_form.get_send_request_button().is_enabled() == False
        with allure.step("Кликаем на кнопку send request"):    
            registration_form.get_send_request_button().click()
        with allure.step("Проверяем что после нажатия на кнопку url не сменился из за неправильного email"):
            assert registration_form.get_url() == 'https://nomia.net/#contact-form'
        
    
    @allure.story('Неуспешная регистрация с вводом валидных данных и пустым полем ввода имени пользователя')
    def test_registration_null_username(self):
        registration_form = RegistrationForm(self.driver)
        try_for_free = registration_form.get_try_for_free_button()
        with allure.step("Кликаем на кнопку try for free"):
            try_for_free.click()
        with allure.step("Проверяем текст кнопки try for free"):
            assert try_for_free.text == 'try for free'
        with allure.step("Оставляем поле ввода имени пустым"):
            registration_form.get_username_field().clear()
        with allure.step("Вводим валидное название компании"):
            registration_form.get_company_name_field().send_keys('company_name')
        with allure.step("Вводим валидный номер телефона"):
            registration_form.get_phone_number_field().send_keys('+7 00000000')
        with allure.step("Вводим валидный email"):
            registration_form.get_email_field().send_keys('testmail@gmail.com')
        with allure.step("Кликаем на кнопку send request"):
            registration_form.get_send_request_button().click()
        with allure.step("Проверяем что появилось сообщение об ошибке (Обязательное поле)"):
            registration_form.get_error_required_field().text == 'Обязательное поле'

    
    @allure.story('Неуспешная регистрация с вводом валидных данных и пустым полем ввода номера телефона')
    def test_registration_null_phone_number(self):
        registration_form = RegistrationForm(self.driver)
        try_for_free = registration_form.get_try_for_free_button()
        with allure.step("Кликаем на кнопку try for free"):
            try_for_free.click()
        with allure.step("Проверяем текст кнопки try for free"):
            assert try_for_free.text == 'try for free'
        with allure.step("Вводим валидное имя пользователя"):
            registration_form.get_username_field().send_keys('username')
        with allure.step("Вводим валидное название компании"):
            registration_form.get_company_name_field().send_keys('company_name')
        with allure.step("Оставляем поле ввода номера телефона пустым"):
            registration_form.get_phone_number_field().clear()
        with allure.step("Вводим валидный email"):
            registration_form.get_email_field().send_keys('testmail@gmail.com')
        with allure.step("Кликаем на кнопку send request"):
            registration_form.get_send_request_button().click()
        with allure.step("Проверяем что появилось сообщение об ошибке (Обязательное поле)"):
            registration_form.get_error_required_field().text == 'Обязательное поле'

    
    @allure.story('Неуспешная регистрация с вводом невалидного номера телефона (буквы вместо чисел)')
    def test_registration_invalid_phone_number(self):
        registration_form = RegistrationForm(self.driver)
        try_for_free = registration_form.get_try_for_free_button()
        with allure.step("Кликаем на кнопку try for free"):
            try_for_free.click()
        with allure.step("Проверяем текст кнопки try for free"):
            assert try_for_free.text == 'try for free'
        with allure.step("Вводим валидное имя пользователя"):
            registration_form.get_username_field().send_keys('username')
        with allure.step("Вводим валидное название компании"):
            registration_form.get_company_name_field().send_keys('company_name')
        with allure.step("Вводим невалидный номер телефона (буквы вместо чисел)"):
            registration_form.get_phone_number_field().send_keys('string')
        with allure.step("Вводим валидный email"):
            registration_form.get_email_field().send_keys('testmail@gmail.com')
        with allure.step("Кликаем на кнопку send request"):
            registration_form.get_send_request_button().click()
        with allure.step("Проверяем что появилось сообщение об ошибке (Некорректное значение)"):
            registration_form.get_error_invalid_symbol().text == 'Некорректное значение'


    

    





    

        
        








