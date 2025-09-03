from page.AuthPage import AuthPage
from pytest_ui_api_template.test.conftest import browser

def test_first(browser):
    auth_page = AuthPage(browser)
    auth_page.go()

def test_auth():	
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("логин", "пароль")

 # Проверяем, что после запуска теста URL заканчивается заданной подстрокой:
    assert auth_page.get_current_url().endswith("...")