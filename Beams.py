import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.170"}
driver = webdriver.Firefox()

class user:
    def __init__(self, email, password, message, teams_link, start_hour):
        self.email = email
        self.password = password
        self.message = message
        self.teams_link = teams_link
        self.start_hour = start_hour

    def var_setup(self):
        link = self.teams_link
        page = requests.get(link, headers=headers)
        driver.get(self.teams_link)

    def login_manager(self, driver):
        time.sleep(5)
        email_field = driver.find_element_by_id("i0116") 
        email_field.send_keys(self.email)
        next_button = driver.find_element_by_id("idSIButton9")
        next_button.click()
        password_field = driver.find_element_by_id("i0118")
        password_field.send_keys(self.password)
        time.sleep(6)
       
    def sign_in_field_input(self, driver):
        sign_in_button = driver.find_element_by_id("idSIButton9")
        sign_in_button.click()
        time.sleep(2)

    def yes_pop_up_clicker(self, driver):
        yes_button = driver.find_element_by_id("idSIButton9")
        yes_button.click()
        time.sleep(5)
       
    def sendMessage(self, driver):
        message_field = driver.find_element_by_class_name("cke_editable")
        message_field.send_keys(self.message)
        time.sleep(2)
        
    def dismiss_pop_clicker(self, driver):
        dismiss_pop_up_field = driver.find_element_by_class_name("text")
        dismiss_pop_up_field.click()
        time.sleep(5)
       
    def press_send_button(self, driver):
        send_button = driver.find_element_by_class_name("icons-send")
        send_button.click()
    
    def start_function(self):
        loopstatus = True
        hours = self.start_hour

        while loopstatus:
            current_time = datetime.datetime.now()

            if hours == current_time.hour:
                loopstatus = False
                self.var_setup()
                self.login_manager(driver)
                self.sign_in_field_input(driver)
                self.yes_pop_up_clicker(driver)
                self.sendMessage(driver)
                self.dismiss_pop_clicker(driver)
                self.press_send_button(driver)

            else:
                pass
                    
user1.start_function()