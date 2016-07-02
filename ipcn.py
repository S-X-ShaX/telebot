#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#from urllib.request import urlopen
from html.parser import HTMLParser

#ipcn = urlopen("http://ip.cn/").read().decode("utf-8")

class IPCNParser(HTMLParser):
    def __init__(self):
        super(IPCNParser,self).__init__()
        self._okay = False
        self._code = 0
        self.result = None

    def handle_starttag(self,tag,attrs):
        if tag == "div" and attrs == [('id', 'result')]:
            self._okay = True
        if self._okay and tag == "code":
            self._code += 1

    def handle_endtag(self,tag):
        if self._okay and tag == "code":
            self._code += 1
        if tag == "div":
            self._okay = False

    def handle_data(self,data):
        if self._okay and self._code == 1:
            self.result = data

#iparser = IPCNParser()

#iparser.feed(ipcn)