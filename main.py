from playwright.async_api import async_playwright, Playwright

def run(playwright: Playwright):
    start_url = "https://nl.indeed.com/jobs?q=python&l=&from=searchOnHP"
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(start_url)

    while True:
        for link in page.locator(
            
        )



