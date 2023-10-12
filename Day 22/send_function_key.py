from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pyrobot import Robot
driver = webdriver.Chrome(executable_path="C:\\Users\\HP 840\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/basic_auth")
# action = ActionChains(driver)
# action.send_keys(Keys.TAB).perform()
# action.send_keys(Keys.TAB).perform()
# action.send_keys(Keys.TAB).perform()
# action.send_keys(Keys.TAB).perform()
robot = Robot()
robot.key_press('tab')
robot.key_release('tab')
