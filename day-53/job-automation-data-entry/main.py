from selenium_webdriver import SeleniumWebDriver
from beautiful_soup import Bs4Scrape

driver = SeleniumWebDriver()
driver.enter_search_criteria()
url = driver.current_url

soup = Bs4Scrape()
soup.get_data_from_html(url)

