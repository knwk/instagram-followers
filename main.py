from selenium import webdriver
from time import sleep
from getpass import getpass

class InstaBot:
    def __init__(self):
        # Retrieve login Info
        self.username = input("Username: ")
        self.password = getpass("Password: ")
        # Automate login
        self.__setup()
        self.__login()
        self.__ignore_popup()
    
    def __setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
    
    def __login(self):
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)
    
    def __ignore_popup(self):
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
    
    def my_profile_page(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]"\
            .format(self.username)).click()
    

    
    

        

my_bot = InstaBot()
my_bot.my_profile_page()
