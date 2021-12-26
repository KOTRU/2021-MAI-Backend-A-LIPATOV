import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options


DRIVER_LOCATION = "/usr/bin/chromedriver" 
BINARY_LOCATION = "/usr/bin/google-chrome" 


class AdminLoginTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.binary_location = BINARY_LOCATION 
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) 


    def test_search_login_button(self):
        driver = self.driver
        driver.get('http://localhost:8000/admin')
        self.assertIn("admin",driver.title)
        submit_row = driver.find_element_by_class_name('submit-row')
        button = submit_row.find_elements_by_xpath(".//*")[1]
        button.click()
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()