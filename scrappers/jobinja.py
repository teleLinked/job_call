import re
from playwright.sync_api import Playwright, sync_playwright, expect
import os
from dotenv import load_dotenv

load_dotenv()



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)