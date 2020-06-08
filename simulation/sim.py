from selenium import webdriver
from time import sleep

from controls import controls

DRIVER_LOCATION = './drivers/edgedriver_win64/msedgedriver.exe'
driver = webdriver.Edge(DRIVER_LOCATION)
driver.get('https://iss-sim.spacex.com/')

begin_button = "//*[@id='begin-button']"


def get_info(info):
    return driver.find_element_by_xpath(info).text


def control(control):
    driver.find_element_by_xpath(control).click()


print('ParrotNAV: Starting Simulation')

sleep(20)

print('ParrotNAV: Entering Simulation')

driver.find_element_by_xpath(begin_button).click()

sleep(10)

control(controls.speed_boost)
print('ParrotNAV: Starting Controller')
