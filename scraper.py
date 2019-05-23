from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get('https://www.jumbo.com/aanbiedingen')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')

images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))

driver.close()
