import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

from utilities.customLogger import LogGen
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()

    username = ReadConfig.getUseremail()

    password = ReadConfig.getPassword()
    l=LogGen.loggen()



    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.l.info("*************test001 home page ttile*********************")

        self.driver=setup
        self.driver.get(self.baseURL)
        title=self.driver.title
        self.l.info("*************verifying*********************")
        if title=="Your store. Login":
            self.l.info("*************Passed*********************")
            self.driver.close()

            assert True
        else:
            self.driver.save_screenshot("C:\Python_Selenium\CommerceNopHybrid\Screenshots\home.png")
            self.l.info("*************Passed*********************")
            self.driver.close()

            assert False
    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        title = self.driver.title



        if title == "Dashboard / nopCommerce administration":

            self.driver.close()

            assert True
        else:
            time.sleep(2)
            self.driver.save_screenshot("C:\Python_Selenium\CommerceNopHybrid\Screenshots\login.png")
            time.sleep(2)
            self.driver.close()
            assert False


