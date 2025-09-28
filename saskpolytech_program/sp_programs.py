#
# Ref.: Rubén Del Campo, Dynamic Web Page Scraping With Python: A Guide to Scrape All Content
# https://www.zenrows.com/blog/dynamic-web-pages-scraping-python#what-is-dynamic-website
#


# pip3 install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_program(driver):

    # find elements by class name 'az-name'
    programs = driver.find_elements(By.CLASS_NAME, 'az-name')

    scraped_data = []

    # iterate over found elements and print their text content
    for program in programs:
        program_item = program.find_element(By.TAG_NAME, 'a',)

        data = {
            'name': program_item.text,
            'url': program_item.get_attribute('href'),
        }

        # append the data to the empty list
        scraped_data.append(data)

    # return the scraped data
    return scraped_data

def scrape_all_page(url):
    # instantiate options for Chrome
    options = webdriver.ChromeOptions()
    # run the browser in headless mode
    options.add_argument('--headless=new')
    # instantiate Chrome WebDriver with options
    driver = webdriver.Chrome(options=options)
    # open the specified URL in the browser
    driver.get(url)
    # get the previous height value
    last_height = driver.execute_script('return document.body.scrollHeight')
    # array to collect scraped data
    data = []
    while True:
        # scroll down to the bottom
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        # wait for the page to load
        time.sleep(2)

        # get the new height and compare it with the last height
        new_height = driver.execute_script('return document.body.scrollHeight')

        if new_height == last_height:
            # extract data once all content has loaded
            data.extend(scrape_program(driver))
            break
        last_height = new_height

    # close the browser
    driver.quit()

    return data


URL = 'https://saskpolytech.ca/programs-and-courses/browse-programs/a-z-listing.aspx'

program_listings = []
program_listings.extend(scrape_all_page(URL))

import pandas as pd
df = pd.DataFrame(program_listings)
print(df)

import sys
sys.exit()

