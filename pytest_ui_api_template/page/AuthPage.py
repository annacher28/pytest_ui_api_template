from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.remote.webdriver import WebDriver

class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.url = "https://trello.com/login"
        self.driver = driver  

    def go(self):
        self.driver.get(self.url)

    def login_as(self, email: str, password: str):
        self.driver.find_element(By.CSS_SELECTOR, "#username-uid1").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#username-uid1").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#password"))
        )
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, by, value):
        return self.driver.find_element(by, value)
