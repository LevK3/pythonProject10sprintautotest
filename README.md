# Тесты на проверку параметра name при создании наборов с продуктами в Яндекс.Прилавок с помощью API Яндекс.Прилавок.
- Все пути храняться в отдельном файле configuration.py.
- Тела POST-запросов вынеси в отдельный файл data.py.
- Все запросы ( создание пользователя и набора) для решения задачи, в одном файле sender_stand_request.py.
- Все тесты по чек-листу (позитивные и негативные) в файле create_kit_name_kit_test.py.
- Для запуска тестов должны быть установлены пакеты pytest и requests.
- Запуск всех тестов выполянется командой pytest.
- Созданы вспомогательные файлы проекта: .gitignore - игнорирует автоматически генерируемые файлы, и README - инструкция по проекту.