import requests
import webbrowser
from bs4 import BeautifulSoup
import smtplib
import timeit
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from threading import Timer
import datetime
#MB
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.170"}
link = "THE LINK OF THE TEAMS CHAT (GROUP)"
driver = webdriver.Firefox()
page = requests.get(link, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
driver.get("THE LINK OF THE TEAMS CHAT (GROUP)")

def start_every_thing():
    time_var_1 = Timer(2.0, login_manager)
    time_var_1.start()

def login_manager():
    email_field = driver.find_element_by_id("i0116") 
    email_field.send_keys("YOUR EMAIL")
    next_button = driver.find_element_by_id("idSIButton9")
    next_button.click()
    password_field = driver.find_element_by_id("i0118")
    password_field.send_keys("YOUR PASSWORD")
    time_var_2 = Timer(6.0, sign_in_field_input)
    time_var_2 .start()

def sign_in_field_input():
    sign_in_button = driver.find_element_by_id("idSIButton9")
    sign_in_button.click()
    time_var_3 = Timer(2.0, yes_pop_up_clicker)
    time_var_3.start()

def yes_pop_up_clicker():
    yes_button = driver.find_element_by_id("idSIButton9")
    yes_button.click()
    time_var_4 = Timer(5.0, sendMessage)
    time_var_4.start()

def sendMessage():
    message_field = driver.find_element_by_class_name("cke_editable")
    message_field.send_keys("YOUR MESSAGE")
    time_var_5 = Timer(2.0, dismiss_pop_clicker)
    time_var_5.start()

def dismiss_pop_clicker():
    dismiss_pop_up_field = driver.find_element_by_class_name("text")
    dismiss_pop_up_field.click()
    time_var_6 = Timer(5.0, press_send_button)
    time_var_6.start()

def press_send_button():
    send_button = driver.find_element_by_class_name("icons-send")
    send_button.click()

loopstatus = True
hours = 8
while loopstatus:
    current_time = datetime.datetime.now()
    if hours == current_time.hour:
        loopstatus = False
        start_every_thing()
    else:
        pass
#MB