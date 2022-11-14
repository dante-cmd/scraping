# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException, WebDriverException
# available since 2.4.0

# Others
import time
from pathlib import Path
from urllib.parse import urljoin
import requests
from lxml.html import fromstring, tostring

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# Set the path of the webdriver
driver_path = r'C:\dmozilla\geckodriver.exe'
ser = Service(driver_path)
opt = FirefoxOptions()

# opt.add_argument('--headless')

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(service=ser, options=opt)

# go to the google home page
driver.get("http://127.0.0.1:5502/scraping/index.html")

obj = driver.switch_to.alert

time.sleep(2)

obj.send_keys('Dante')

time.sleep(1)

obj.accept()

time.sleep(1)

print(driver.page_source)
#Retrieve the message on the Alert window
# message=obj.text
# print ("Alert shows following message: "+ message )

driver.quit()

# # # find the element that’s name attribute is q (the google search box)
# # inputElement = driver.find_element(By.NAME, value = "q")

# # # type in the search
# # inputElement.send_keys("Cheese!")

# # # submit the form (although google automatically searches now without submitting)
# # inputElement.submit()

# # # the page is ajaxy so the title is originally this:
# # print(driver.title)

# # # we have to wait for the page to refresh, the last thing that seems to be updated i
# # try:
# #     WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith('ch'))
# #     # You should see "cheese! - Google Search"
# #     print(driver.title)
# #     time.sleep(5)
# #     driver.quit()

# # except:
# #     time.sleep(5)
# #     driver.quit()
