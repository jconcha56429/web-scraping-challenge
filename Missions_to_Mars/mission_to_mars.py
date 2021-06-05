#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import nbconvert
import requests
import time
from splinter import Browser

# In[2]:

def scrape ():
        
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[3]:


    url = "https://redplanetscience.com/"
    browser.visit(url)


    # In[4]:


    html = browser.html
    soup = bs(html, "html.parser")


    # In[5]:


    title = soup.find('div', class_='content_title').get_text()
    paragraph = soup.find('div', class_='article_teaser_body').get_text()


    # In[6]:


    url = "https://spaceimages-mars.com"
    browser.visit(url)
    html2 = browser.html
    soup = bs(html2,"html.parser")


    # In[7]:


    featured_img = soup.find('div', class_='header')


    # In[8]:


    featured_img


    # In[9]:


    jpg = featured_img.find('a', class_="showimg fancybox-thumbs")
    jpg = jpg['href']


    # In[10]:


    featured_img = (f'{url}/{jpg}')


    # In[11]:


    featured_img


    # In[12]:


    url = 'https://galaxyfacts-mars.com/'


    # In[13]:


    # browser.visit(url)
    # html3 = browser.html


    # In[14]:


    tables = pd.read_html(url)


    # In[15]:


    table = tables[1]


    # In[16]:


    df = pd.DataFrame(table)


    # In[17]:


    mars_facts_html = df.to_html()


    # In[18]:


    mars_facts_html


    # In[19]:


    url = 'https://marshemispheres.com/'
    browser.visit(url)
    html4 = browser.html
    soup = bs(html4,"html.parser")


    # In[20]:


    hemis = soup.find_all('div', class_='description')
    for hemi in hemis:
        print(hemi.find('h3').get_text())


    # In[21]:


    # In[ ]:





    # In[22]:


    url="https://marshemispheres.com/"
    browser.visit(url)


    # In[23]:


    hemisphere_image_urls  = []
    my_dict = {'name':[],'title':[]}
    for x in range(0,4):
        browser.links.find_by_partial_text('Hemisphere')[x].click()
        html = browser.html
        soup = bs(html,'html.parser')
        title = soup.find('h2', class_='title').get_text()
        test = soup.find('img', class_='wide-image')
        img_url = url+test['src']
        my_dict = {'Title':title,'url':img_url}
        hemisphere_image_urls.append(my_dict)
        browser.back()


    # In[24]:


    print(hemisphere_image_urls) 


    # In[26]:


    browser.quit()


    # In[ ]:




