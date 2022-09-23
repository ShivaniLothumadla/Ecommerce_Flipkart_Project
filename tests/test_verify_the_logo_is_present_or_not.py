import pytest
from pages.loginpage import LoginPage
from utilities.utilities import Utility


class Test_Verify_the_logo_present_or_not:

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

    def test_002_verify_the_logo_is_present(self):
        """
        The logo should be displayed
        """
        self.ut.assertTrue(self.lp.home.logo.is_displayed(), msg='Logo is not displayed')
        self.log.info('user is in homepage and able to see the flipkart logo')
