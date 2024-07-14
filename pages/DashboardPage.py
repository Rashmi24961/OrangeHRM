from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self,driver):
        self.driver=driver

    Dashboard_text_xpath="//h6[text()='Dashboard']"

    def verify_Dashboard_text(self,driver):
        self.driver.find_element(By.XPATH,self.Dashboard_text_xpath).is_displayed()



