from playwright.sync_api import sync_playwright,Route,Request, Response
import csv
import time
import re
li_selector_pattern = '//*[@id="js-jobSearchPaginator"]/div/ul/li[a]/a/text()'

def get_next_page_button(page):
    next_page_button = page.query_selector(re.sub(r'\[a\]', '[0-9]+', li_selector_pattern))
    return next_page_button

def insert_into_csv(li_elements):
    with open('list_items.csv', 'a', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['List Items'])  
        for li in li_elements:
            csv_writer.writerow([li.strip()])  

def get_li_elements(page):
    for attempt in range(3):  # Retry up to 3 times
        try:
            li_elements = page.query_selector_all('#js-jobSeekerSearchResult > div > div:nth-child(2) > section > div > ul > li')
            if li_elements:
                return [li.inner_text() for li in li_elements]
        except Exception as e:
            print(f"Attempt {attempt+1}: Failed to locate elements - {e}")
            time.sleep(3)  # Wait for 3 seconds before retrying
    return [] 

def scrape_and_insert(url):
   
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url, timeout=60000)  

            page.wait_for_selector('//*[@id="js-jobSeekerSearchResult"]/div/div[2]/section/div/ul')

            while True:
                li_elements = get_li_elements(page)
                insert_into_csv(li_elements)
                GREEN = '\033[92m'
                RESET = '\033[0m'
                print(GREEN + "List items inserted into CSV file."+ RESET)

                page.wait_for_selector('//*[@id="js-jobSearchPaginator"]/div/ul')

                dynamic_next = get_next_page_button(page)
                if dynamic_next:
                    dynamic_next.click()
                    page.wait_for_load_state('networkidle')
                else:
                    print("No dynamic next link found. Exiting loop.")
                break
                
        browser.close()
           