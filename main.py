from playwright.sync_api import sync_playwright
import csv

def insert_into_csv(li_elements):
    with open('list_items.csv', 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['List Items'])  
        for li in li_elements:
            csv_writer.writerow([li.strip()])  

def get_li_elements(page):
    li_elements = page.query_selector_all('#js-jobSeekerSearchResult > div > div:nth-child(2) > section > div > ul > li')
    return [li.inner_text() for li in li_elements]

def scrape_and_insert(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, timeout=60000)  

        page.wait_for_selector('//*[@id="js-jobSeekerSearchResult"]/div/div[2]/section/div/ul')

        li_elements = get_li_elements(page)
        insert_into_csv(li_elements)
        print("List items inserted into CSV file.")
        
        next_link = page.query_selector('//*[@id="js-jobSearchPaginator"]/div/ul/li[12]/a')
        while next_link:
            next_link.click()
            page.wait_for_load_state('networkidle')

      
            li_elements = get_li_elements(page)
            insert_into_csv(li_elements)
            print("List items inserted into CSV file.")

        
            next_link = page.query_selector('//*[@id="js-jobSearchPaginator"]/div/ul/li[12]/a')

        browser.close()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, timeout=60000)  

        page.wait_for_selector('//*[@id="js-jobSeekerSearchResult"]/div/div[2]/section/div/ul')

        while True:
            li_elements = get_li_elements(page)
            insert_into_csv(li_elements)
            print("List items inserted into CSV file.")

            next_link = page.query_selector('//*[@id="js-jobSearchPaginator"]/div/ul/li[12]/a')

            if not next_link:
                break

            next_link.click()

            page.wait_for_load_state('networkidle')

            page.wait_for_selector('//*[@id="js-jobSeekerSearchResult"]/div/div[2]/section/div/ul/li')

        browser.close()

if __name__ == "__main__":
    url = "https://jobinja.ir/jobs"
    scrape_and_insert(url)
