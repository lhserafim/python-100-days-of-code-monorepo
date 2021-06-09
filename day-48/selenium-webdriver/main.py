from selenium import webdriver

CHROME_DRIVER_PATH = "/Volumes/Macintosh HD 1/Estudos/Python/100-days-of-code/day-48/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://www.amazon.com.br/Macbook-Apple-Retina-Radeon-Espacial/dp/B07R7S26J8/ref=sr_1_17?__mk_pt_BR=%C3"
           "%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=macbook&qid=1623226448&refinements=p_89%3AApple&rnid"
           "=18120432011&s=computers&sr=1-17")  # Abre o navegador com a URL digitada

price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)

search_bar = driver.find_element_by_name("field-keywords")
print(search_bar.tag_name)
print(search_bar.get_attribute("name"))

logo_icon = driver.find_element_by_class_name("nav-logo-link")
print(logo_icon.size)

# Probably one of the easiest ways to get the information
# Colocar o . para indicar que é uma classe
# Colocar # para indicar que é um id
# e depois a tag
customer_reviews = driver.find_element_by_css_selector("#acrCustomerReviewLink span")
print(customer_reviews.text)

# Minha escolha, copiar o xPath do html
print(driver.find_element_by_xpath("//*[@id='acrCustomerReviewText']").text)
print(driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]/div[10]/div/div/div/div/div/div[2]/div/div["
                                   "2]/div/ol/li[5]/div[1]/div/a/span").text)


profiles = driver.find_elements_by_class_name("a-profile-name")

for name in profiles:
    print(name.text)

# Transformando em um dicionário
names = {}
for n in range(len(profiles)):
    names[n] = {
        "name": profiles[n].text
    }

print(names)


driver.close()  # fecha uma tab
driver.quit()  # fecha todas as tabs
