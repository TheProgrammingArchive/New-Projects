from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://indianexpress.com/section/india/').text

soup = BeautifulSoup(source, features='lxml')
# print(soup.prettify())

cs_file = open('cms_scrapedata.csv', 'w+')
cs_write = csv.writer(cs_file)
cs_write.writerow(['', 'SUMMARY', 'SOURCE', 'DATE', 'TITLE'])

for articles in soup.find_all('div', class_='articles'):
    # print(articles)
    title = articles.find('h2', class_='title').text
    print(title)

    summary = articles.p.text
    print(summary)

    date = articles.find('div', class_='date').text
    print(date)

    source = articles.h2.a['href']
    print(source)

    cs_write.writerow(['', summary, source, date, title])
cs_file.close()

