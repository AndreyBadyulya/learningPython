from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('before_method')
class TestLogin:

	@pytest.fixture(scope="class")
	def before_class(self, request):
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.implicitly_wait(10)
		request.cls.driver = driver
		yield driver
		driver.quit()

	@pytest.fixture()
	def before_method(self, request, before_class):
		request.cls.driver.get('http://the-internet.herokuapp.com/')

	def  test_wait_for_visibility(self):
		self.driver.find_element_by_link_text('Dynamic Loading').click()
		self.driver.find_element_by_partial_link_text('Example 1').click()
		finish_message = self.driver.find_element_by_id('finish')
		assert not finish_message.is_displayed()
		start_button = self.driver.find_element_by_css_selector('#start button')
		start_button.click()
		wait = WebDriverWait(self.driver, 15)
		wait.until(lambda driver: not start_button.is_displayed())
		#wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#start button'))
		assert not start_button.is_displayed()
		wait.until(EC.visibility_of(finish_message))
		assert finish_message.is_displayed()

	def  test_wait_for_invisibility(self):
		self.driver.find_element_by_link_text('Dynamic Loading').click()
		self.driver.find_element_by_partial_link_text('Example 2').click()
		assert not self.driver.find_elements_by_id('finish')
		start_button = self.driver.find_element_by_css_selector('#start button')
		start_button.click()
		wait = WebDriverWait(self.driver, 15)
		wait.until(lambda driver: not start_button.is_displayed())
		assert not start_button.is_displayed()
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#finish')))
		assert self.driver.find_elements_by_id('finish')