#!/usr/bin/env python3
#coding: utf-8

import requests, html, sys
from bs4 import BeautifulSoup

useage = "useage: python3 getter.py agc055 chodkudai a"

if len(sys.argv) < 4:
    print(useage)
    sys.exit()
    
def end():
    sleep(0.5)
    sys.exit(1)

def checksource(url, html):
    soup = BeautifulSoup(html.content, "html.parser")
    x = []  
    links = soup.find_all('a')
    for link in links:
        x.append(link.get('href'))
    
    url = []
    count = 0
    for i, j in enumerate(x):
        string = str(j)
        if('task' in string):
            count = count + 1
        if(count >= 2 and str(sys.argv[3])  == string[-1::]):
            url = str(x[i+4])
            return url

def makesource(url):
    req = "https://atcoder.jp" + url
    html = requests.get(req)
    soup = BeautifulSoup(html.content, "html.parser")
    print(soup.pre.string)

def main():
    try:
        print
        url =  "https://atcoder.jp/contests/" + sys.argv[1] + "/submissions?f.Status=AC&f.User=" + sys.argv[2]
        html = requests.get(url)
        sourceurl = checksource(url, html)
        makesource(sourceurl)
    except KeyboardInterrupt:    
        end()

if __name__ == '__main__':
    main()
