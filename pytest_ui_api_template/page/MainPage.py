from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    # Получаем текущий URL
    def get_current_url(self) -> str:
        return self.driver.current_url

    # Нажимаем на иконку с именем в верхнем правом углу
    def open_menu(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            "account-menu-popover-content "
        ).click()

    # Получаем информацию о пользователе (имя и email)
    def get_account_info(self) -> list[str]:
        container = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div[class='ERJaovT43JFwpy'] > div"
        )
        fields = container.find_elements(By.CSS_SELECTOR, "div")
        name = fields[0].text
        email = fields[1].text
        return [name, email]
