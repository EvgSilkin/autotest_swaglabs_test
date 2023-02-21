### В этом репозитории расположен проект-портфолио по автоматизации тестирования покупки двух товаров через UI-интерфейс на тестовом сайте [SWAGLABS](https://www.saucedemo.com/).

#### Проект реализован на языке программирования Python.
#### В проекте задействованы следующие пакеты (и их зависимости):
- selenium
- pytest
- pytest-order
- webdriver-manager
- allure

### Подключение и настройка проекта на локальном компьютере:
- Клонировать проект на локальный компьютер
- Перейти в корневой каталог проекта
- Создать виртуальное окружение:
_File - Settings - Project: name - Python Interpreter - Add interpreter_
- Перейти в виртуальное окружение с помощью ввода в терминале команды: `venv/Scripts/activate`
- Установить пакеты и зависимости с помощью ввода в терминал команды: `pip install -r requirements.txt`
- Запустить тест с помощью ввода в терминал команды: `python -m pytest --alluredir=test_results/ test/`
- Отобразить allure-отчет, после выполнения проверок с помощью ввода в терминал команды: `allure serve test_results/`



[Ссылка на портфолио](https://docs.google.com/document/d/1qqiY6eE5F0_nukb1E979TQb4SeIlW6y7y4AQ6zcDu28/edit "QA Engineer | Тестировщик – Силкин Евгений")



