from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import random
import time

outfile = open("bonus_lijst.html", "w") #open new html file

options = Options()
options.headless = True #set options for driver

driver = webdriver.Chrome(options=options)

driver.get('https://www.ah.nl/bonus') #URL to scrape

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2) #wait for page to load
delay = 10

try:
   myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="epp_index_10"]/article[10]')))
   print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")        #check if loading is done correctly

products = driver.find_elements_by_class_name('product-cardview--bonus-group')
style = driver.find_elements_by_tag_name('head')

outfile.write("<!doctype html>" +"\n" + "<html>" + "\n") #Write HTML file

styleHTML = str(style[0].get_attribute("innerHTML"))
outfile.write(styleHTML + "\n")

for i in range(3):
    randomnumber = random.randint(0,len(products)-1)
    product = products[randomnumber]
    nextline = str(product.get_attribute("innerHTML"))
    outfile.write(nextline + "\n")

outfile.write("</html>")

driver.close()

