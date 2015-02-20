
# coding: utf-8

# GotDrawn
# 
# Taking getsdrawndotcom code and adding in features such as comments.
# Getting rid of folder structure. 

# In[49]:

import os
import requests

import re
import json
import arrow

import praw

import dominate

from dominate.tags import * 

import shutil



# In[28]:

gotdrndir = ('/home/wcmckee/gotdrawn')


# In[29]:

r = praw.Reddit(user_agent='getsdrawndotcom')


# In[30]:

fulcom = []
fuldic = dict()


# In[31]:

getrn = r.get_subreddit('redditgetsdrawn')


# In[32]:

rnew = getrn.get_new()


# In[42]:

for rnc in rnew:
    fulcom.append(rnc)


# In[44]:

artes = arrow.utcnow()


# In[48]:

print artes.date()


# In[51]:

os.chdir('/home/wcmckee/gotdrawn/')


# In[54]:

for flc in fulcom:
    if 'http://i.imgur.com' in flc.url:
        print flc.title
        print flc.url
        print flc.author
        res = requests.get(flc.url, stream=True)
        with open(str(flc.author) + '-' + str(artes.date()) + '-reference.png', 'wb') as outfil:
            shutil.copyfileobj(res.raw, outfil)
            del res
            
        for flcz in flc.comments:
            print flcz


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



