from selenium import webdriver
import pytest
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        login_page=LoginPage(self.driver)
        login_page.implicit_wait()
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_on_login_button(driver=None)
        login_page.implicit_wait()
        expected_text = "Dashboard"
        dashboard_page=DashboardPage(self.driver)
        assert dashboard_page.verify_Dashboard_text(driver=None).__eq__(expected_text)

    def test_login_with_invalid_username_and_valid_password(self):
        login_page = LoginPage(self.driver)
        login_page.implicit_wait()
        login_page.enter_username("Admin Abc")
        login_page.enter_password("admin123")
        login_page.click_on_login_button(driver=None)
        expected_warning_message="Invalid credentials"
        assert login_page.retrieve_warning_message(driver=None).__eq__(expected_warning_message)

    def test_login_with_without_entering_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.implicit_wait()
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_on_login_button(driver=None)
        # login_page.implicit_wait()
        # expected_warning_message = "Invalid credentials"
        # assert login_page.retrieve_warning_message().__eq__(expected_warning_message)




