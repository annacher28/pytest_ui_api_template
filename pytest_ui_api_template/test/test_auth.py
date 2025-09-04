from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager 
from pytest_ui_api_template.page.AuthPage import AuthPage
from page.AuthPage import AuthPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from page.MainPage import MainPage

def test_first():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(4)
    browser.maximize_window()

    auth_page = AuthPage(browser)
    auth_page.go()

def test_auth(browser: WebDriver):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("cherepanovaanna2006@gmail.com", "AnnaCher28%%")
    
    two_factor_form = WebDriverWait(auth_page.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".css-17f7621"))
    )
    assert two_factor_form is not None

def auth_test(browser):	
    email = "Anna28"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("cherepanovaanna2006@gmail.com", "AnnaCher28%%")

    #Создаем главную страницу:
    main_page = MainPage(browser)
    #Открываем иконку с пользователем в правом верхнему углу:
    main_page.open_menu()
    #Открываем информацию о пользователе:
    info = main_page.get_account_info()

    assert main_page.get_current_url().endswith("https://trello.com/u/_anna_cherepanova_/boards")
    assert info[0] == "Anna28"
    assert info[1] == email