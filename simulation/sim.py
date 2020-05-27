from selenium import webdriver
from time import sleep

driver = webdriver.Edge(
    '/mnt/c/Users/raad1/Documents/Webdrivers/edgedriver_win64/msedgedriver.exe')
driver.get('https://iss-sim.spacex.com/')

def control(control):
    driver.find_element_by_xpath(control).click()

sleep(30)

# driver.find_element_by_xpath(pitch_up).click()

# while True:
#     print(driver.find_element_by_xpath('//*[@id="x-range"]/div').text)
