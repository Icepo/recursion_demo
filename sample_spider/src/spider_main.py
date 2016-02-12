# coding:utf-8

# 总调度
import url_manager

import html_downloader

import html_parser

import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, url):
        count = 1
        self.urls.add_new_url(url)
        while self.urls.has_new_url():
            current_url = self.urls.get_new_url()
            print 'crawl    %d  :   %s' % (count, current_url)
            count += 1
            if count == 10:
                break
            html_content = self.downloader.download(current_url)
            if html_content is None:
                continue
            new_urls, new_data = self.parser.parse(current_url, html_content)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)
        self.outputer.output()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
