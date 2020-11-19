from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')
driver.switch_to.frame("login_frame")

driver.find_element_by_id('u').send_keys("1850115698@qq.com")
driver.find_element_by_id('p').send_keys('start$0123.')
driver.find_element_by_id('login_button').click()
time.sleep(5)