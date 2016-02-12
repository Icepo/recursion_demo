# coding:utf-8
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def __init__(self):
        pass

    def parse(self, url, html_content):
        if url is not None and html_content is not None:
            soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
            new_urls = self._get_new_urls(url, soup)
            new_data = self._get_new_data(url, soup)
            return new_urls, new_data

    @staticmethod
    def _get_new_urls(url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(url, soup):
        res_data = {}

        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_='lemma-summary')
        if summary_node is None or len(summary_node.get_text()) == 0:
            summary_node = soup.find('div', class_='para')

        res_data['summary'] = summary_node.get_text()

        res_data['page_url'] = url

        return res_data
