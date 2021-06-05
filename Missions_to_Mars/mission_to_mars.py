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


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:





# In[ ]:





# In[3]:


def mars_news():
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    title = soup.find('div', class_='content_title').get_text()
    paragraph = soup.find('div', class_='article_teaser_body').get_text()
    return(f'{title}: {paragraph}')


# In[4]:


mars_news()


# In[5]:


def featured():
    url = "https://spaceimages-mars.com"
    browser.visit(url)
    html2 = browser.html
    soup = bs(html2,"html.parser")
    featured_img = soup.find('div', class_='header')
    jpg = featured_img.find('a', class_="showimg fancybox-thumbs")
    jpg = jpg['href']
    featured_img = (f'{url}/{jpg}')
    featured_img

    return(featured_img)

featured()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[6]:


def mars_facts():
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    table = tables[1]
    df = pd.DataFrame(table)
    mars_facts_html = df.to_html()
    mars_facts_html = bs(mars_facts_html,"html.parser")
    return(mars_facts_html)


# In[7]:


mars_facts()


# In[8]:


#url = 'https://marshemispheres.com/'
#browser.visit(url)
#html4 = browser.html
#soup = bs(html4,"html.parser")
#hemis = soup.find_all('div', class_='description')
# for hemi in hemis:
#     print(hemi.find('h3').get_text())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:


def hemispheres():
    url="https://marshemispheres.com/"
    browser.visit(url)
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
    return(hemisphere_image_urls)


# In[10]:


hemispheres()


# In[11]:


def scrape():
    data = {"Title & Paragraph":mars_news(),
            "Feautured Image":featured(),
            "Mars Facts": mars_facts(),
            "Hemispheres":hemispheres()}
    return(data)


# In[12]:


scrape()


# In[13]:
