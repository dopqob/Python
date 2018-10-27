#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 12:26
# @Author  : Bilon
# @File    : html_outputer.py
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>{}</td>'.format(data['url']))
            fout.write('<td>{}</td>'.format(data['title']))
            fout.write('<td>{}</td>'.format(data['summary']))
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')