import os
import time

from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver

Keys

desired_caps = {
                # 'platformName': 'iOS',
                'platformName': 'Android',
                'platformVersion': '6.0.1',
                'deviceName': 'HT48NWZ02491',
                'browserName': 'Chrome',
                'noReset': True
                }

# 開啟app
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 前往目標網址
# driver.get('http://game.granbluefantasy.jp/#mypage')

# driver.get('https://www.google.com/')  # https://lmgtfy.com/
driver.get('https://irs.thsrc.com.tw/IMINT/')  # https://lmgtfy.com/
#
# time.sleep(5)
#
# q = driver.find_element_by_name('q')
# q.send_keys('appium')
#
# from selenium.webdriver.common.keys import Keys
#
# q.send_keys('\ue006')
# # q.send_keys(Keys.RETURN)
#
#
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(driver.page_source, 'lxml')
#
# for ele in soup.select('.LC20lb'):
#     print(ele.text)

driver.save_screenshot('ttt.png')  #將目標網頁存成圖片
ele = driver.find_element_by_id('BookingS1Form_homeCaptcha_passCode')

print(ele.location)
print(ele.size)


l = ele.location['x']
r = ele.location['x'] + ele.size['width']

t = ele.location['y']
b = ele.location['y'] + ele.size['height']

print(l, r, t, b)


from PIL import Image
im = Image.open("ttt.png")
im.show()
im = im.crop((l, t, r, b))
im.show()


# time.sleep(15)

driver.quit()

