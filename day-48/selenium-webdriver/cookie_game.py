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
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

# Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break

