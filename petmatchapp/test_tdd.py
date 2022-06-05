from django.test import LiveServerTestCase
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time


class TestSupport(LiveServerTestCase):
    def testSupport(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)

        driver.get('http://127.0.0.1:8000/settings/')
        button = driver.find_element_by_name("support") 
        button.click()

        assert 'Settings' in driver.title

        driver.close()