#!/usr/bin/env python
import gtk
import webkit
import warnings
import gobject
gobject.threads_init()

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
        print "working"

    def crawl(self):
        view = WebView()
        view.open(self._url)
        view.connect('load-finished', self._finished_loading)
        self.add(view)
        gtk.main()

    def _finished_loading(self, view, frame):
        with open(self._file, 'w') as f:
            p = view.get_html()
            #beaut = jsbeautifier.default_options(p)
            f.write(p)
            print p

        gtk.main_quit()

def main():
    #set save location and url target to scrape
    file1= "bbc.txt"
    url1 = "https://www.bbc.co.uk/"
    crawler = Crawler(url1, file1)
    crawler.crawl()
    print "done....."


if __name__ == '__main__':
    main()