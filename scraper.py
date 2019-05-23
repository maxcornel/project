from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.ah.nl/bonus')

driver.close()