from selenium import webdriver
from time import sleep


driver = webdriver.Edge(
    '/mnt/c/Users/raad1/Documents/Webdrivers/edgedriver_win64/msedgedriver.exe')
driver.get('https://iss-sim.spacex.com/')

translate_left = '//*[@id="translate-left-button"]'
translate_right = '//*[@id="translate-right-button"]'
translate_up = '//*[@id="translate-up-button"]'
translate_down = '//*[@id="translate-down-button"]'
translate_forward = '//*[@id="translate-forward-button"]'
translate_backward = '//*[@id="translate-backward-button"]'
yaw_left = '//*[@id="yaw-left-button"]'
yaw_right = '//*[@id="yaw-right-button"]'
pitch_up = '//*[@id="pitch-up-button"]'
pitch_down = '//*[@id="pitch-down-button"]'
roll_left = '//*[@id="roll-left-button"]'
roll_right = '//*[@id="roll-right-button"]'

sleep(30)

# driver.find_element_by_xpath(pitch_up).click()

# while True:
#     print(driver.find_element_by_xpath('//*[@id="x-range"]/div').text)
