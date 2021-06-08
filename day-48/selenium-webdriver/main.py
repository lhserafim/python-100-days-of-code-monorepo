from selenium import webdriver

CHROME_DRIVER_PATH = "/Volumes/Macintosh HD 1/Estudos/Python/100-days-of-code/day-48/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://www.amazon.com")  # Abre o navegador com a URL digitada

driver.close()  # fecha uma tab
driver.quit()  # fecha todas as tabs
