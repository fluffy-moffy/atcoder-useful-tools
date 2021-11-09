import requests, html, sys
from bs4 import BeautifulSoup

url =  "https://atcoder.jp/contests/" + sys.argv[1] + "/submissions?f.Status=AC&f.User=" + sys.argv[2]
html = requests.get(url)
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
        break

req = "https://atcoder.jp" + url
html = requests.get(req)
soup = BeautifulSoup(html.content, "html.parser")
print(soup.pre.string)
