# coding:utf-8


class UrlManager(object):
    # 构造方法中指定两个列表一个存储待爬取的地址 一个存储已爬取的地址
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 增加一个待爬取地址
    def add_new_url(self, url):
        if url is not None and url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        temp_url = self.new_urls.pop()
        self.old_urls.add(temp_url)
        return temp_url

    # 批量增加方法
    def add_new_urls(self, urls):
        if urls is not None and len(urls)>0:
            for url in urls:
                self.add_new_url(url)