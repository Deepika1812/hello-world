import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
browser=webdriver.Chrome(executable_path='/usr/bin/chromedriver')
browser.get('https://www.flipkart.com')
wait=WebDriverWait(browser,10)
element=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'_2zrpKA')))
element.send_keys("9515129203")
browser.find_element_by_xpath("//input[@type=\"password\"]").send_keys("Deepu5a6")
browser.find_element_by_xpath("//button[@class='_2AkmmA _1LctnI _7UHT_c']").click()
"""def search_items(str):
    wait2=WebDriverWait(browser,10)
    element2=wait2.until(EC.presence_of_element_located((By.CLASS_NAME,'LM6RPg')))
    element2.send_keys(str)
    element2.click()
search_items("televisions")"""
