from django.test import LiveServerTestCase
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

class testHome(LiveServerTestCase):

    def test(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get('https://pet-match-fds.herokuapp.com')

        assert 'PetMatch' in driver.title
        time.sleep(2)

class invalidLog(LiveServerTestCase):
    def testInvalid(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get('https://pet-match-fds.herokuapp.com/accounts/login/')
        
        user_name = driver.find_element_by_id('id_login')
        password = driver.find_element_by_id('id_password')

        user_name.send_keys('seleniuminvalid')
        password.send_keys('passwordinvalid')

        driver.find_element_by_class_name('btn-success').click() 

class blankLog(LiveServerTestCase):
    def testBlank(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get('https://pet-match-fds.herokuapp.com/accounts/login/')
        driver.find_element_by_class_name('btn-success').click() 

class testSignup(LiveServerTestCase):

    def testSign(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get('https://pet-match-fds.herokuapp.com/accounts/signup/')

        user_name = driver.find_element_by_id('id_username')
        email = driver.find_element_by_id('id_email')
        password1 = driver.find_element_by_id('id_password1')
        password2 = driver.find_element_by_id('id_password2')

        user_name.send_keys('Seleniumtest')
        email.send_keys('selenium@gmail.com')
        password1.send_keys('momentanio')
        password2.send_keys('momentanio')
        driver.find_element_by_class_name('btn-success').click()
        time.sleep(2)

class testLogin(LiveServerTestCase):

    def testLog(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get('https://pet-match-fds.herokuapp.com/accounts/login/')

        user_name = driver.find_element_by_id('id_login')
        password = driver.find_element_by_id('id_password')

        user_name.send_keys('Seleniumtest')
        password.send_keys('momentanio')

        driver.find_element_by_class_name('btn-success').click()


        add = driver.find_elements_by_class_name('nav-link')
        add[0].click()

        pet_name = driver.find_element_by_id('id_name')
        pet_age = driver.find_element_by_id('id_age')
        pet_race = driver.find_element_by_id('id_race')
        pet_bio = driver.find_element_by_id('id_bio')

        pet_name.send_keys('Mel')
        pet_age.send_keys('8')
        pet_race.send_keys('Mestiço')
        pet_bio.send_keys('Mel gosta de correr pelo parque e morder almofadas')
        driver.find_element_by_class_name('btn-success').click()
        time.sleep(5)

        home = driver.find_elements_by_class_name('navbar-brand')
        home[0].click()
        

        driver.close()