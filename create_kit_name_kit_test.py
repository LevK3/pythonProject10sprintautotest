# Импортируем необходимые библиотеки и модули
import sender_stand_request

import data


# Функция возврата токена
def get_new_user_token():
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = new_user_response.json()["authToken"]
    return auth_token


# Функция для изменения значения в параметре name в теле запроса
def get_kit_body(name):
    # Копируется словарь с телом запроса из файла data
    current_kit_body = data.kit_body.copy()
    # Изменение значения в поле name
    current_kit_body["name"] = name
    # Возвращается новый словарь с нужным значением name
    return current_kit_body


# Функция для позитивной проверки
def positive_assert(name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    # В переменную auth_token сохраняем полученный токен
    auth_token = get_new_user_token()
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == name


# Функция негативной проверки
def negative_assert_code_400(kit_body):
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())

    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400


# Тест 1 Допустимое количество символов в имени набора (1)
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert("a")


# Тест 2 Допустимое количество символов в имени набора (511)
def test_create_kit_511_letter_in_kit_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3 Ошибка. Количество символов меньше допустимого в имени набора (0)
def test_create_kit_0_letter_in_kit_name_get_error_response():
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body("")
    # Проверка полученного ответа
    negative_assert_code_400(kit_body)


# Тест 4 Ошибка. Количество символов больше допустимого в имени набора (512)
def test_create_kit_512_letter_in_kit_name_get_error_response():
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    # Проверка полученного ответа
    negative_assert_code_400(kit_body)


# Тест 5 Разрешены английские буквы в имени набора (QWErty)
def test_create_kit_english_letter_in_kit_name_get_success_response():
    positive_assert("QWErty")


# Тест 6 Разрешены русские буквы в имени набора (Мария)
def test_create_kit_russian_letter_in_kit_name_get_success_response():
    positive_assert("Мария")


# Тест 7 Разрешены спецсимволы в имени набора ("№%@",)
def test_create_kit_has_special_symbol_letter_in_kit_name_get_success_response():
    positive_assert('"№%@",')


# Тест 8 Разрешены пробелы в имени набора ( Человек и КО )
def test_create_kit_has_space_letter_in_kit_name_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9 Разрешены цифры в имени набора (123)
def test_create_kit_has_number_letter_in_kit_name_get_success_response():
    positive_assert("123")


# Тес 10 Ошибка. Параметр имени набора не передан в запросе ()
def test_create_kit_empty_in_kit_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)


# Тест 11 Ошибка. Передан другой тип параметра имени набора (число)
def test_create_kit_number_type_in_kit_name_get_error_response():
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(123)
    # Проверка полученного ответа
    negative_assert_code_400(kit_body)



