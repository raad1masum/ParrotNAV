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


def translate_left():
    driver.find_element_by_xpath(translate_left).click()


def translate_right():
    driver.find_element_by_xpath(translate_right).click()


def translate_up():
    driver.find_element_by_xpath(translate_up).click()


def translate_down():
    driver.find_element_by_xpath(translate_down).click()


def translate_forward():
    driver.find_element_by_xpath(translate_forward).click()


def translate_backward():
    driver.find_element_by_xpath(translate_backward).click()


def yaw_left():
    driver.find_element_by_xpath(yaw_left).click()


def yaw_right():
    driver.find_element_by_xpath(yaw_right).click()


def pitch_up():
    driver.find_element_by_xpath(pitch_up).click()


def pitch_down():
    driver.find_element_by_xpath(pitch_down).click()


def roll_left():
    driver.find_element_by_xpath(roll_left).click()


def roll_right():
    driver.find_element_by_xpath(roll_right).click()


sleep(30)

# driver.find_element_by_xpath(pitch_up).click()

# while True:
#     print(driver.find_element_by_xpath('//*[@id="x-range"]/div').text)
