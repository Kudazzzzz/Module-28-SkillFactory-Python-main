# Module-28-SkillFactory-Python
Rostelekom

Итоговый проект по автоматизации тестирования на курсе QAP в Skillfactory

Задание:
Протестировать требования.
Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
Провести обеспеченность тестированием продукта (не менее 20 автотестов).
Оформить описание обнаруженных дефектов. Если дефекты не обнаружены, подумайте и опишите 3 потенциальных дефекта на специализированном ресурсе.

• Мною были протестированы требования заказчиков, которые не совсем корректны с сайтом. 


По оформлению требований хочу отметить:
некоторые пункты имели отступы, а некоторые нет;
названия некоторых полей выделены по разному (курсив, подчеркивание, жирный текст).

• Разработаны тест-кейсы и потенциальные баги.
• При разработке тест-кейсов были применены следующие техники тест-дизайна: 
эквивалентное разбиение, 
анализ граничных значений, 
таблица принятия решений, 
диаграмма перехода состояния http://joxi.ru/DmBk8Z7I68x652 ,
попарное тестирование (Pairwise).

• Отчет создан с помощью инструмента Google-таблицы: https://docs.google.com/spreadsheets/d/1WLSEvACCroPUsTlWz-otTkgjpNaU9nbA2ybVQLxuRNQ/edit?usp=sharing
• В ходе теста дефекты не найдены, навык оформления баг-репортов на примере: https://docs.google.com/spreadsheets/d/1Z-b-OxhtTIq1FnOpt66qyf2eVCNfS2d5JNHalKReuU8/edit?usp=sharing

• Были написаны автотесты.
• Для тестирования сайта был использован интсрумент Selenium.
• Для определения локаторов использовались следующие инструменты: DevTools, Element Locator.
• При написании автотестов дополнительно установлены библиотеки: pytest, selenium, pytest-selenium.
Запуск тестов:
Установить все требования: pip install -r requirements.txt
Загрузите свой Selenium WebDriver с  (выберите версию, совместимую с вашим браузером)
Запустить тест: python -m pytest -v --driver Chrome --driver-path /tests/chromedriver.exe tests/test_rostelekom.py
