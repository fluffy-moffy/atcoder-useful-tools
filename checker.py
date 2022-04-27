#!/usr/bin/env python3
#coding: utf-8

import requests, html
import sys
from bs4 import BeautifulSoup

usage = "usage: python3 checker.py agc055 chokudai"

logo = '''
 ###                ###      ###                ##
  ##                 ##       ##               ####
  ##       ####      ##       ##      ####     ####
  #####   ##  ##     ##       ##     ##  ##     ##
  ##  ##  ######     ##       ##     ##  ##     ##
  ##  ##  ##         ##       ##     ##  ##
 ###  ##   #####    ####     ####     ####      ##
'''

if len(sys.argv) < 3:
    print(usage)
    sys.exit()

def end():
    time.sleep(0.5)
    sys.exit(1)

def checkcode(url, html):
	x = []
	soup = BeautifulSoup(html.content, "html.parser")
	for tag in soup.select('td')[1::10]:
	    problemid = tag.text
	    x.append(problemid)
	return x

def cleancode(results):
	for string in results:
		print(string)

def main():
	try:
		print(logo)
		url = "https://atcoder.jp/contests/" + sys.argv[1] + "/submissions?f.Status=AC&f.User=" + sys.argv[2]
		html = requests.get(url)
		results = checkcode(url, html)
		cleancode(results)
	except KeyboardInterrupt:
		end()

if __name__ == '__main__':
	main()
