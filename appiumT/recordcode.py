# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "6.0.1"
caps["deviceName"] = "FA667BN01350"
caps["appPackage"] = "com.PChome.Shopping"
caps["appActivity"] = ".MainActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

TouchAction(driver).tap(x=377, y=1977).perform()
TouchAction(driver).press(x=738, y=1254).move_to(x=707, y=2116).release().perform()

TouchAction(driver).tap(x=93, y=320).perform()
TouchAction(driver).tap(x=397, y=175).perform()
TouchAction(driver).tap(x=1063, y=1796).perform()
TouchAction(driver).tap(x=681, y=1048).perform()
TouchAction(driver).tap(x=305, y=356).perform()
TouchAction(driver).tap(x=625, y=898).perform()

driver.quit()