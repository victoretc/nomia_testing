from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement

import allure

class RegistrationForm(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver 
        self.__try_for_free_button: str = "//button[@title='try for free']"
        self.__username_field: str = "//input[@name='userName']"
        self.__company_name_field: str = "//input[@name='companyName']"
        self.__phone_number_field: str = "//input[@name='phone']"
        self.__email_field: str = "//input[@name='email']"
        self.__send_request_button: str = "//button[contains(text(),'Send request')]"
        self.__agreement_button: str = "//input[@name='checkAgreement']"  #Нужно добавить негативный тест кейс с регистрацией без нажатия чек - бокса
        self.__sucess_form: str = "//div[contains(@class, 'modal active')]" #//div[contains(@class, 'modal__title')] = заявка отпрвлена , //div[contains(@class, 'modal__text')] , //div[contains(@class, 'modal__icon')] 

    @allure.step('Получение кнопки try for free')
    def get_try_for_free_button(self) -> WebElement:
        return self.is_visible('xpath', self.__try_for_free_button, 'Try for free button')

    @allure.step('Получение поля для ввода имени пользователя')
    def get_username_field(self) -> WebElement:
        return self.is_visible('xpath', self.__username_field, 'Username Field')

    @allure.step('Получение поля для ввода названия компании')
    def get_company_name_field(self) -> WebElement:
        return self.is_visible('xpath', self.__company_name_field, 'Company Name Field')
   
    @allure.step('Получение поля для ввода номера телефона')
    def get_phone_number_field(self) -> WebElement:
        return self.is_visible('xpath', self.__phone_number_field, 'Phone Number Field')
    
    @allure.step('Получение поля для ввода пользовательской почты')
    def get_email_field(self) -> WebElement:
        return self.is_visible('xpath', self.__email_field, 'Email Field')

    @allure.step('Получение кнопки для отправки информации из формы')
    def get_send_request_button(self) -> WebElement:
        return self.is_visible('xpath', self.__send_request_button, 'Send Request Button')
    
    @allure.step('Получение чек бокса для соглашения с политикой компании')
    def get_agreement_button(self) -> WebElement:
        return self.is_visible('xpath', self.__agreement_button, 'Agreement Check Box')
    
    @allure.step('Получение формы успешной отправки данных')
    def get_success_form(self) -> WebElement:
        return self.is_visible('xpath', self.__sucess_form, 'Sucess Form') #нужно расширить тесты с проверкой содержимого формы успеха

    def get_url(self):
        return self.driver.current_url


   
    
    



    

    
    
    
    
    
    
    
    
    # username_field: str = "//input[@name='userName']"
    # company_name_field: str = "//input[@name='companyName']"
    # phone_number_field: str = "//input[@name='phone']"
    # email_field: str = "//input[@name='email']"
    # send_request_button: str = "//button[contains(text(),'Send request')]"






