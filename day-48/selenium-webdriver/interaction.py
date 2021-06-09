from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Preciso desta importação para enviar o ENTER

CHROME_DRIVER_PATH = "/Volumes/Macintosh HD 1/Estudos/Python/100-days-of-code/day-48/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal")  # Abre o navegador com a URL digitada

# Clicando usando a pesquisa pelo xpath
artigos = driver.find_element_by_xpath("//*[@id='mw-content-text']/div[1]/div[1]/div/div[1]/table/tbody/tr/td["
                                       "2]/div/p/a[1]")
# artigos.click()

# Clicando usando método mais especifico e melhor
# driver.find_element_by_link_text("Portais").click()

# Digitando informações
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()  # fecha todas as tabs