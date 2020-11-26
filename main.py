import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import re

#change the filename below
df=pd.read_csv('testurls.csv')


def getLinks(url):
    try:
        html_page = requests.get(url,timeout=60)
        soup = str(BeautifulSoup(html_page.text,'lxml'))
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', soup)
        for i in urls:
            if 'instagram' in i:
                return i

    except:
        return -1

    return -1

insta_urls=[]
url=[]
for i in df['url']:
    url.append(i)
    print("Extracting",i)
    insta_urls.append(getLinks(i))



with open("output.csv", "w",newline='',encoding="utf-8") as csvFile:
    fieldnames = ['url','Instagram']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    for u,insta in zip(url,insta_urls):
        writer.writerow({'url':u,'Instagram':insta})