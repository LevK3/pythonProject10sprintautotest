# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests

# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импорт данных запроса из модуля data, в котором определены заголовки, тело запроса и тело набора
import data


# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# Определение функции post_new_client_kit для отправки POST-запроса на создание нового набора пользователя
def post_new_client_kit(kit_body, auth_token):
    new_auth_headers = data.headers.copy()
    new_auth_headers["Authorization"] = f"Bear {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=new_auth_headers)








