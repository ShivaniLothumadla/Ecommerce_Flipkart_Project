from selenium.webdriver.common.by import By
from pages.homepage import HomePage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    _close_icon_xpath = "//button[contains(text(),'✕')]"
    _login_dialog_xpath = '//*[@class="_2QfC02"]'
    _username_xpath = "//span[contains(text(),'Enter Email/Mobile number')]//parent::label//parent::div//input[@type='text']"
    _password_xpath = "//span[contains(text(),'Enter Password')]//parent::label//parent::div//input[@type='password']"
    _login_button_xpath = "//span[ text()='Login']//parent::button[@type='submit']"


    @property
    def close_icon(self):
        return self.driver.find_element(By.XPATH, self._close_icon_xpath)

    @property
    def login_dialog(self):
        return self.driver.find_element(By.XPATH, self._login_dialog_xpath)

    def username(self, value):
        return self.driver.find_element(By.XPATH, self._username_xpath).send_keys(value)

    def password(self, value):
        return self.driver.find_element(By.XPATH, self._password_xpath).send_keys(value)

    @property
    def login(self):
        return self.driver.find_element(By.XPATH, self._login_button_xpath)

    @property
    def home(self):
        return HomePage(self.driver)
