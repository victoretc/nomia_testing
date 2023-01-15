import pytest
import allure
import time

from selenium.webdriver.common.alert import Alert
from page_objects.registration_form import RegistrationForm

@pytest.mark.usefixtures('setup')
class TestRegistrationForm():
    
    @pytest.mark.skip("Проверяем другой тест")
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
        
        
        





    

        
        










    # driver.find_element(By.XPATH, RegistrationForm.username_field).send_keys('test_username')
    # driver.find_element(By.XPATH, RegistrationForm.company_name_field).send_keys('test_company_name')
    # driver.find_element(By.XPATH, RegistrationForm.phone_number_field).send_keys('+7 00000000')
    # driver.find_element(By.XPATH, RegistrationForm.email_field).send_keys('test_mail@gmail.com')
    # driver.find_element(By.XPATH, RegistrationForm.send_request_button).click()
    # assert 1 == 1

