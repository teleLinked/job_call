from playwright.sync_api import sync_playwright,Route,Request, Response
import csv
import time


def insert_into_csv(li_elements):
    with open('list_items.csv', 'a', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['List Items'])  
        for li in li_elements:
            lenth = len(li)
            csv_writer.writerow([lenth])
            csv_writer.writerow([li.strip()])  
            csv_writer.writerow(["\n ---------------------------------------- \n"])

def get_li_elements(page):
    # Attempt to locate the elements with a retry mechanism
    for attempt in range(3):  # Retry up to 3 times
        try:
            li_elements = page.query_selector_all('#js-jobSeekerSearchResult > div > div:nth-child(2) > section > div > ul > li')
            if li_elements:
                return [li.inner_text() for li in li_elements]
        except Exception as e:
            print(f"Attempt {attempt+1}: Failed to locate elements - {e}")
            time.sleep(3)  # Wait for 3 seconds before retrying
    return [] 

def on_request(request: Request):
    pass

def on_response(response: Response):
    pass

def on_route(route: Route):
    route.abort()

def scrape_and_insert(url):
   
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url, timeout=60000)  

            page.wait_for_selector('//*[@id="js-jobSeekerSearchResult"]/div/div[2]/section/div/ul')

            while True:
                li_elements = get_li_elements(page)
                insert_into_csv(li_elements)
                print("List items inserted into CSV file.")

                next_link = page.query_selector('//*[@class="aginator-next-text"]')

                if not next_link:
                    break

                next_link.click()

                page.wait_for_load_state('networkidle')
                
        browser.close()
                # page.wait_for_selector('//*[@id="js-jobSeekerSearchResult"]/div/div[2]/section/div/ul/li')
                # page.wait_for_selector('#js-jobSeekerSearchResult > div > div:nth-child(2) > section > div > ul > li',timeout=60000)
