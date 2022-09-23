from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    _logo_xpath = '//*[@title="Flipkart"]'
    _login_button_xpath = "//a[contains(text(),'Login')] | //body/div[@id='container']/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]"
    _logout_button_xpath = "//div[contains(text(),'Logout')]"
    _search_xpath = "//*[@title='Search for products, brands and more']"

    @property
    def logo(self):
        return self.driver.find_element(By.XPATH, self._logo_xpath)

    @property
    def login(self):
        return self.driver.find_element(By.XPATH, self._login_button_xpath)

    @property
    def logout(self):
        return self.driver.find_element(By.XPATH, self._logout_button_xpath)
