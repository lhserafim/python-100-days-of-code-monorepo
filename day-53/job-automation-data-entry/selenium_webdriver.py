from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time


CHROME_DRIVER_PATH = "/Volumes/Macintosh HD 1/Estudos/Python/100-days-of-code/day-53/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
# driver.get("https://www.zillow.com/")
driver.get("https://www.zillow.com/homes/for_sale/Salt-Lake-City,-UT_rb/")


class SeleniumWebDriver:
    def __init__(self):
        self.current_url = ""

    def enter_search_criteria(self):
        try:
            search_bar = driver.find_element_by_id("search-box-input")
            search_bar.send_keys("Salt Lake City")
            search_bar.send_keys(Keys.SPACE)
            search_bar.send_keys(Keys.BACKSPACE)
            time.sleep(2)
            driver.find_element_by_id("react-autowhatever-1--item-0").click()
            time.sleep(2)
            if driver.find_element_by_xpath("/html/body/div[8]/div/div[1]/div/div/div/ul/li[3]/button"):
                driver.find_element_by_xpath("/html/body/div[8]/div/div[1]/div/div/div/ul/li[3]/button").click()
        except UnexpectedAlertPresentException:
            driver.get("https://www.zillow.com/homes/for_sale/Salt-Lake-City,-UT_rb/")
        except NoSuchElementException:
            driver.get("https://www.zillow.com/homes/for_sale/Salt-Lake-City,-UT_rb/")
        finally:
            self.current_url = driver.current_url
