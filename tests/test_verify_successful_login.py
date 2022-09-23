import pytest
from pages.loginpage import LoginPage
from utilities.utilities import Utility


class Test_verify_successful_login:

    @pytest.fixture(autouse=True)
    def setup_class(self):
        """
        importing the classes which will used as part of the test case development.
         Made it fixture because instead of creating objects in the test steps, it will be organized in one place and can be used whenever required.
        """
        self.driver = self.driver
        self.lp = LoginPage(self.driver)
        self.ut = Utility()
        self.log = self.ut._loggers()

    def test_001_launch_the_browser(self):
        """Launching the browser
            closing the login up
        """
        self.lp.close_icon.click()  # closing the login page as when i launch the browser getting login pop in Automation browser
        self.log.info('User is in homepage')

    def test_002_click_on_login_button(self):
        """
        Login dialog should be displayed
        """
        self.ut.assertTrue(self.lp.home.login.is_displayed(), msg='Login button is not displayed')
        self.lp.home.login.click()
        self.ut.assertTrue(self.lp.login_dialog.is_displayed(), msg='Login Dialog is not displayed')
        self.log.info('User is clicked on login button and login dialog is appeared')

    def test_003_enter_data_and_click_on_submit(self):
        """
        Login should be successful
        """
        # the provided username and passwords are dummy, please replace with the original credentials to get logged in
        self.lp.username('9876543246')
        self.lp.password('Ytrewq91')
        self.lp.login.click()
        self.ut.assertTrue(self.lp.home.logo.is_displayed(), msg='Logo is not displayed')
        self.log.info('user is logged in and able to see the flipkart logo')
