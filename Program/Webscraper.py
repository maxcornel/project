from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

def getproducts():
    options = Options()
    options.headless = True                                         #set options for driver
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.ah.nl/bonus')                                          #URL to scrape

    ActionChains(driver).move_to_element(driver.find_elements_by_class_name("link-notice__image"))
    time.sleep(3)                                                   #wait for page to load
    delay = 5

    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="epp_index_10"]/article[10]')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")                         #check if loading is done correctly

    productslist = driver.find_elements_by_xpath("//*[@class='edc-container legend grid-item small-12 large-3 xlarge-2_4 xxlarge-2 legend--single edc-container--color-bonus column' or @class='product column product--searchandbrowse promotion-theme--ah product-cardview small-6 medium-6 large-3 xlarge-2_4 xxlarge-2 product-cardview--bonus-group' or @class='product column product--searchandbrowse promotion-theme--ah product-cardview small-6 medium-6 large-3 xlarge-2_4 xxlarge-2']")

    products = {}
    for i in range(len(productslist)):
        products[i] = str(productslist[i].get_attribute('outerHTML'))
    driver.close()
    return products

def getid():
    options = Options()
    options.headless = True  # set options for driver
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.ah.nl/bonus')  # URL to scrape

    ActionChains(driver).move_to_element(driver.find_elements_by_class_name("link-notice__image"))
    time.sleep(3)  # wait for page to load
    delay = 5

    try:
        myElem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="epp_index_10"]/article[10]')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")  # check if loading is done correctly

    productslist = driver.find_elements_by_xpath("//*[@class='edc-container legend grid-item small-12 large-3 xlarge-2_4 xxlarge-2 legend--single edc-container--color-bonus column' or @class='product column product--searchandbrowse promotion-theme--ah product-cardview small-6 medium-6 large-3 xlarge-2_4 xxlarge-2 product-cardview--bonus-group' or @class='product column product--searchandbrowse promotion-theme--ah product-cardview small-6 medium-6 large-3 xlarge-2_4 xxlarge-2']")
    productid = {}
    for i in range(len(productslist)):                          #make dictionary of all ID
        productid[i] = str(productslist[i].get_attribute('id'))

    productidnum = {}                                           #get usefull IDs
    for i in productid:
        if productid[i] != '':
            productidnum[i] = productid[i]

    IDnum = {}
    for k, v in productidnum.items():
        IDnum[v] = k

    driver.close()
    return IDnum

def getstyle():
    options = Options()
    options.headless = True                                         # set options for driver
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.ah.nl/bonus')                           # URL to scrape
    style = driver.find_elements_by_tag_name('head')
    styleHTML = str(style[0].get_attribute("innerHTML"))            #copy the style of the site
    driver.close()
    return styleHTML


