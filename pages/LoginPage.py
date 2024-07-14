from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver=driver


    username_field_xpath = "//input[@name='username']"
    password_field_xpath = "//input[@name='password']"
    login_button_xpath = "//button[@type='submit']"
    warning_message_xpath = "//p[text()='Invalid credentials']"

    def enter_username(self,username_text):
        self.driver.find_element(By.XPATH, self.username_field_xpath).click()
        self.driver.find_element(By.XPATH, self.username_field_xpath).clear()
        self.driver.find_element(By.XPATH,self.username_field_xpath).send_keys(username_text)


    def enter_password(self, password_text):
        self.driver.find_element(By.XPATH, self.password_field_xpath).click()
        self.driver.find_element(By.XPATH, self.password_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password_text)


    def click_on_login_button(self, driver):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()


    def retrieve_warning_message(self, driver):
        return self.driver.find_element(By.XPATH,self.warning_message_xpath).text

    def implicit_wait(self):
        self.driver.implicitly_wait(5)

