from playwright.sync_api import Playwright, sync_playwright, expect
import os

email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://jobinja.ir/login/user")
    page.get_by_placeholder("آدرس ایمیل خود را وارد نمایید").click()
    page.get_by_placeholder("آدرس ایمیل خود را وارد نمایید").fill(email)
    page.get_by_placeholder("رمز عبور خود را وارد نمایید").click()
    page.get_by_placeholder("رمز عبور خود را وارد نمایید").fill(password)
    page.get_by_role("button", name="وارد شوید").click()

    context.storage_state(
        path= "playwright/.auth/auth.json"
    )
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
