from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import random

outfile = open("bonus_lijst.html", "w")

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get('https://www.ah.nl/bonus')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
delay = 3 # seconds

try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="epp_index_10"]/article[10]')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

products = driver.find_elements_by_class_name('product-cardview--bonus-group')

outfile.write("<!doctype html>" +"\n" + "<html>" + "\n")


for product in products:
    nextline = str(product.get_attribute("outerHTML"))
    outfile.write(nextline + "\n")

outfile.write("</html>")

driver.close()

