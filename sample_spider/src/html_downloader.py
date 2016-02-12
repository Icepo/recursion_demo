# coding:utf-8
import urllib2


class HtmlDownloader(object):
    @staticmethod
    def download(url):
        if url is not None:
            response = urllib2.urlopen(url)
            if response is not None and response.getcode() == 200:
                return response.read()
