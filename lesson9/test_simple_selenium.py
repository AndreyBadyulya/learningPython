from selenium import webdriver
import pytest

@pytest.mark.usefixtures('before_method')
class TestLogin:

    @pytest.fixture(scope="class")
    def before_class(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        request.cls.driver = driver
        yield driver
        #driver.quit()

    @pytest.fixture()
    def before_method(self, request, before_class):
        request.cls.driver.get('http://the-internet.herokuapp.com/')

    def test_login(self):
        self.driver.find_element_by_link_text('Form Authentication').click()
        username_input = driver.find_element_by_id('username')
        username_input.send_keys('tomsmith')
        password_input = driver.find_element_by_id('password')
        password_input.send_keys('SuperSecretPassword!')
        self.driver.find_element_by_css_selector('::before').click()