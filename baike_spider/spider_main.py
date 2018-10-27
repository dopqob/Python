#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 12:25
# @Author  : Bilon
# @File    : spider_main.py
from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, num):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw {} : {}'.format(count, new_url))
                html_cont = self.downloader.download(new_url)

                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)

                # new_data = self.parser.parse(html_cont)
                self.outputer.collect_data(new_data)

                if count == num:
                    break
                count += 1
            except:
                print('craw failed')

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url, 100)
