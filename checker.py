import requests, html, sys
from bs4 import BeautifulSoup

url =  "https://atcoder.jp/contests/" + sys.argv[1] + "/submissions?f.Status=AC&f.User=" + sys.argv[2]
html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")

X = []

for tag in soup.select('td')[1::10]:
    problemid = tag.text
    X.append((problemid))

print(X)
