from scrappers.jobinja import scrape_and_insert


def main():
    """ Run the whole script ! """
    url = "https://jobinja.ir/jobs"
    scrape_and_insert(url)


if __name__ == "__main__":
    main()
