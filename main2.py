from playwright.sync_api import sync_playwright

#Import Playwright

with sync_playwright() as p:

#Choose a browser, such as Chromium

    browser = p.chromium.launch(headless=False)

    #Create a page object

    my_page = browser.new_page()

    #Change the URL to the site you want for your Playwright web scraping project

    my_page.goto("https://jobinja.ir/")

    #Create an object to contain the content of the page

    page_content = my_page.content()

    #For example purposes, simply print the page contents to the terminal or shell

    print(page_content)

    #Close the browser

    browser.close()