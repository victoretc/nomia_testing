# nomia_testing
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt 

pytest -s -v --alluredir=alureress - запускаем тесты и генерируем отчет allure

allure serve alureress - запускаем отчет allure

Если не установлен allure 

1) Установить Java
2) Установить Allure




