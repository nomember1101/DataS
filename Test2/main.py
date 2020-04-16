from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time
browser = webdriver.Chrome()
url='https://www.dcard.tw/f'
browser.get(url)
inputElement=browser.find_element_by_tag_name('input')
inputElement.send_keys('Python')
browser.find_element_by_css_selector('button.sc-1ehu1w3-2').click()
time.sleep(2)
html=browser.page_source
soup=bs(html,'html.parser')

meta_data=[]
for x in soup.find_all('span',{'class':'sc-6oxm01-2 hiTIMq'}):
    meta_data.append(x.text.strip())
forum=[]
author=[]
time=[]
for i in range (len(meta_data)):
    if i%3==0:
        forum.append(meta_data[i])
    elif i%3==1:
        author.append(meta_data[i])
    else :
        time.append(meta_data[i])
print(forum)
print(author)
print(time)
titles=[]
for x in soup.find_all('h2',{'class':'sc-1v1d5rx-3 eihOFJ'}):
    titles.append(x.text)
print(titles)
hrefs=[]
for i in soup.find_all('a',{'class':'sc-1v1d5rx-4 gCVegi'}):
    hrefs.append(i['href'])
print(hrefs)
link=[]
for href in hrefs:
    link.append(urljoin(url,href))
print(link)
