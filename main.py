from selenium import webdriver
from time import sleep
from getpass import getpass

class InstaBot:
    def __init__(self):
        # Retrieve login info
        self.username = input("Username: ")
        self.password = getpass("Password: ")
        # Automate login and navigate to profile
        self.__setup()
        self.__login()
        self.__ignore_popup()
        self.__my_profile_page()
    
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
    
    def __my_profile_page(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{username}')]"\
            .format(username = self.username)).click()
        sleep(4)
    
    def __scroll_accounts(self):
        init_scroll = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[10]")
        self.driver.execute_script('arguments[0].scrollIntoView()', init_scroll)
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        close = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")
        close.click()
        return names

    def get_followers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        sleep(2)
        followers = self.__scroll_accounts()
        return followers

    def get_following(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sleep(2)
        following = self.__scroll_accounts()
        return following

    def details(self):
        followers = self.get_followers()
        following = self.get_following()
        not_following = []
        not_following_back = []
        for user in followers:
            if(user not in following):
                not_following.append(user)
        for user in following:
            if(user not in followers):
                not_following_back.append(user)
        print("Users you do not follow back: ")
        print(not_following)
        print("Users not following you back: ")
        print(not_following_back)

        
# Testing
my_bot = InstaBot()
my_bot.details()
