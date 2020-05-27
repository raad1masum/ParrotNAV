from selenium import webdriver
from time import sleep

DRIVER_LOCATION = '/mnt/c/Users/raad1/Documents/Webdrivers/edgedriver_win64/msedgedriver.exe'
driver = webdriver.Edge(DRIVER_LOCATION)
driver.get('https://iss-sim.spacex.com/')


def get_info(info):
    return driver.find_element_by_xpath(info).text


def control(control):
    driver.find_element_by_xpath(control).click()


sleep(30)

# driver.find_element_by_xpath(pitch_up).click()

# while True:
#     print(driver.find_element_by_xpath('//*[@id="x-range"]/div').text)
