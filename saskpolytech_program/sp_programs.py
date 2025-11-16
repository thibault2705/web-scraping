#
# Ref.: Rubén Del Campo, Dynamic Web Page Scraping With Python: A Guide to Scrape All Content
# https://www.zenrows.com/blog/dynamic-web-pages-scraping-python#what-is-dynamic-website
#


# pip3 install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_programs(driver):
    # find elements by class name 'az-info'
    program_infos = driver.find_elements(By.CLASS_NAME, 'az-info')

    programs = []

    # iterate over found elements
    for info in program_infos:
        name = info.find_elements(By.CLASS_NAME, 'az-name')[0]
        link = name.find_element(By.TAG_NAME, 'a',)
        location = info.find_elements(By.CLASS_NAME, 'az-locations')[0]
        credential = info.find_elements(By.CLASS_NAME, 'az-credential')[0]

        program = {
            'name': name.text,
            'link': link.get_attribute('href'),
            'locations': location.text,
            'credential': credential.text,
        }

        # append the data to the empty list
        programs.append(program)

    # return the scraped data
    return programs

def scrape_whole_page(url):
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
            data.extend(scrape_programs(driver))
            break
        last_height = new_height

    # close the browser
    driver.quit()

    return data


import pandas as pd

def main():
    url = 'https://saskpolytech.ca/programs-and-courses/browse-programs/a-z-listing.aspx'
    programs = scrape_whole_page(url)

    df = pd.DataFrame(programs)
    print(f'Columns: {df.columns}')
    print(f'Shape: {df.shape}')

    df.to_csv('sp_programs.csv', index=False)

if __name__ == '__main__':
    main()

