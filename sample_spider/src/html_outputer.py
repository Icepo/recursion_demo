# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is not None:
            self.datas.append(data)

    def output(self):
        out = open('../output/index.html', 'w')
        out.write('<html>')
        out.write('<body>')
        out.write('<table>')

        for data in self.datas:
            out.write('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (data['page_url'], data['title'].encode('utf-8'), data['summary'].encode('utf-8')))

        out.write('</table>')
        out.write('</body>')
        out.write('</html>')

        out.close()
