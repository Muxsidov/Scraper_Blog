import requests
from bs4 import BeautifulSoup

link = "https://www.scrapethissite.com/pages/"
request = requests.get(link)

soup = BeautifulSoup(request.content, "html5lib")

f = open("data.csv",'w')

f.write(soup.h1.text)
for i in soup.find_all('h3'):
    f.write(i.text)

for i in soup.find_all(class_='lead session-desc'):
    f.write(i.text)

f.close()

# Get .text from <title> tag
# print(soup.title.text)

# Hyperlinks with .a tag
# print(soup.a)

# .find_all()
# for i in soup.find_all('h3'):
#     print(i.text)

# Search with CSS classes
# for i in soup.find_all(class_='lead session-desc'):
#     print(i.text)