# Selenium
# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Others
import time
from pathlib import Path
from operator import getitem


# Set the path of the webdriver
driver_path = r'C:\dmozilla\geckodriver.exe'
ser = Service(driver_path)
opt = Options()

# selenium without opening browser
#  opt.headless = True

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(service=ser, options=opt)

# 1. Go to the link
url = "https://www.metro.pe/"
driver.get(url)


def is_loaded_html():

    counter = 1
    try:
        # Add the element that we want to localize
        seconds = 10
        value = ".text-category-home"
        localized_element = WebDriverWait(driver, seconds).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, value)))

        if localized_element:
            return True
    except:
        # Try only 2 times (20 seconds, 10 seconds each time)
        assert counter <= 2, "The time to localize the HTML is reached"
        counter += 1
        print('Element HTML not localized, run again!')
        is_loaded_html()


def fill_form():
    if is_loaded_html():

        #  1. Localize the click elements
        seconds = 10

        value = ""

        clickable_elements = WebDriverWait(driver, seconds).until(
            EC.element_to_be_clickable((By.XPATH, value)))

        assert len(clickable_elements) == 4, "There is any clickable element"

        (select_element, number_element, location_element,
         button_element) = clickable_elements

        # 1.1
        select_element.click()
        time.sleep(1)

        # find the select element to click
        xpath = ""
        selected = driver.find_element(By.XPATH, xpath)
        selected.click()
        time.sleep(1)

        # 1.2

        # 1.2.1 activate input to sent values
        location_element.click()

        # 1.2 find the select element to sent company
        xpath_to_find_company = ""
        company_element = driver.find_element(By.XPATH, xpath_to_find_company)
        company_value = ""
        company_element.send_keys(value=company_value)
        time.sleep(1)

        # 1.3
        # 1.3.1 Activate input to sent number
        number_element.click()

        # 1.3.2 find the number element to sent the number
        xpath_to_find_number = ""
        number_element = driver.find_element(By.XPATH, xpath_to_find_number)
        number_value = ""
        number_element.send_keys(value=number_value)
        time.sleep(1)

        # 1.4 submit the fields and cteate the windows
        button_element.click()


def download_html():

    # 1. fill form and create a new window
    fill_form()

    # 2. Get the windows and click elements to see the text
    windows = driver.window_handles

    assert len(windows) == 2, "No window have been created"

    # 2.1 Switch to window and finding elements clickable

    new_window = getitem(windows, 1)
    driver.switch_to.window(new_window)

    def get_clickable_elements(value):
        clickable_elements = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, value)))
        return clickable_elements

    xpath = ""
    clickable_elements = get_clickable_elements(xpath)

    for element in clickable_elements:
        element.click()
        time.sleep(1)

    # 2.2 download html file

    page_source = driver.page_source

    path_download = ""
    with open(path_download, 'w', encoding='utf-8') as page:
        page.write(page_source)

    print('file downloaded!!!')


if __name__ == "__main__":
    download_html()
