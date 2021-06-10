#
# 1. Go to the game website and familiarise yourself with how it works:
#
# http://orteil.dashnet.org/experiments/cookie/ (classic version)
#
# 2. Create a bot using Selenium and Python to click on the cookie as fast as possible.
#
#
# 3. Every 5 seconds, check the right-hand pane to see which upgrades are affordable and purchase the most expensive
# one. You'll need to check how much money (cookies) you have against the price of each upgrade.
#
# e.g. both Grandma and Cursor are affordable as we have 103 cookies, but Grandma is the more expensive one,
# so we'll purchase that instead of the cursor.
#
#
# HINT 1: https://www.w3schools.com/python/ref_string_split.asp
#
# HINT 2: https://www.w3schools.com/python/ref_string_strip.asp
#
# HINT 3: https://www.w3schools.com/python/ref_string_replace.asp
#
# HINT 4: https://stackoverflow.com/questions/13293269/how-would-i-stop-a-while-loop-after-n-amount-of-time
#
# 4. After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second". e.g. this is
# mine:
#
#
# 5. Once you've managed to get the bot to work, feel free to tweak the algorithm if you think there is a better way
# to play the game. e.g. Change the time, instead of every 5 seconds to check the upgrades, what if you did every
# second. Or maybe the bot should buy all the affordable upgrades. Post your algorithm in the Q&A and impress us all
# if you manage to get a higher cookies/second with your algo.

from selenium import webdriver
import time

CHROME_DRIVER_PATH = "/Volumes/Macintosh HD 1/Estudos/Python/100-days-of-code/day-48/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Get cookie to click on.
cookie = driver.find_element_by_id("bigCookie")
items = driver.find_elements_by_css_selector("#products div")
item_ids = [item.get_attribute("id") for item in items]

while True:
    cookie.click()
    print(item_ids)

