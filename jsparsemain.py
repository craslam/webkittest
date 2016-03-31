#!/usr/bin/env python
import gtk
import webkit
import warnings
import sys
import gobject
gobject.threads_init()
from optparse import OptionParser

warnings.filterwarnings('ignore')

class WebView(webkit.WebView):
    def get_html(self):
        self.execute_script('oldtitle=document.title;document.title=document.documentElement.innerHTML;')
        html = self.get_main_frame().get_title()
        self.execute_script('document.title=oldtitle;')
        return html

class Crawler(gtk.Window):
    def __init__(self, url, file):
        gtk.gdk.threads_init()
        gtk.Window.__init__(self)
        self._url = url
        self._file = file

    def crawl(self):
        view = WebView()
        view.open(self._url)
        view.connect('load-finished', self._finished_loading)
        self.add(view)
        gtk.main()

    def _finished_loading(self, view):
        with open(self._file, 'w') as f:
            f.write(view.get_html())
        gtk.main_quit()

def main():

    #URL to scrape
    url = "https://pypi.python.org/pypi/jsbeautifier"

    #
    file = "hello.txt"
    crawler = Crawler(url, file)
    crawler.crawl()

if __name__ == '__main__':
    main()