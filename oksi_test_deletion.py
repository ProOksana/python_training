# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://localhost/addressbook/")
    wd.find_element_by_name("user").click()
    wd.find_element_by_name("user").clear()
    wd.find_element_by_name("user").send_keys("admin")
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").clear()
    wd.find_element_by_name("pass").send_keys("secret")
    wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
    if not wd.find_element_by_id("13").is_selected():
        wd.find_element_by_id("13").click()
    wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
    wd.find_element_by_link_text("home").click()
    wd.find_element_by_link_text("Logout").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
