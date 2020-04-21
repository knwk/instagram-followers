from selenium import webdriver
from time import sleep
from getpass import getpass

class InstaBot:
    def __init__(self):
        # Retrieve login Info
        username = input("Username: ")
        password = getpass("Password: ")
        # Automate login
        self.__setup()
        self.__login(username, password)
    
    def __setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
    
    def __login(self, username, password):
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)

my_bot = InstaBot()
