from bs4 import BeautifulSoup

import requests


class Jobinja:
    """ Class to scrap jobinja jobs """

    def __init__(self):
        self.base_url = "https://jobinja.ir/jobs"
        self.headers = {}

    def search_on(self, by_word: str = '',
                  by_location: str = '', by_category: str = ''):
        url = self.base_url + \
            f"?filters[keywords][]={by_word}&filters[locations][]={by_location}&filters[job_categories][]={by_category}"
        print(url)
        response = requests.get(url)
        bs = BeautifulSoup(response.text, "html.parser")
        titles = bs.findAll("a", {"class": "c-jobListView__titleLink"})
        meta_datas = bs.findAll("ul", {"class": "o-listView__itemComplementInfo"})
        print(meta_datas)
        for metadata in meta_datas:
            print(metadata.decode_contents())
        for title in titles:
            print(title.decode_contents())

    def task_on_search_alert(self, by_word: str, by_location: str, by_category: str, every: str):
        ...


jobinja = Jobinja()
jobinja.search_on('Django',)