
# coding: utf-8

# make rst
# 
# Create GetsDrawn post of images

# In[231]:

import requests
import bs4
import json
import arrow
import praw
import os

import ntpath


# In[208]:

r = praw.Reddit(user_agent='getsdrawndotcom')


# In[209]:

rsubred = r.get_subreddit('redditgetsdrawn')


# In[210]:

rsunewq = rsubred.get_new()


# In[211]:

for rsubcom in rsubred.get_comments():
    print (rsubcom)
    #if (rsubcom.author) != 'ItWillBeMine':
    #    print (rsubcom)
    #    print (rsubcom.author)
    
    #answer != 'hi':   # not equal
    #   print "no hi"
    #print (rsubcom.author)


# In[212]:

arnowz = arrow.now()


# In[213]:

ardat = arnowz.date()


# In[214]:

str(ardat)


# In[215]:

artim = arnowz.time()


# In[216]:

#regetd = requests.get('http://getsdrawn.com')


# In[217]:

requgetdrn = open('/home/wcmckee/getsdrawndotcom/index.html', 'r')


# In[218]:

bst = bs4.BeautifulSoup(requgetdrn.read())


# In[219]:

requgetdrn.close()


# In[220]:

bst.find('a')


# In[221]:

alimg = bst.find_all('a')
    #print(bs)


# In[224]:

'''
for ali in alimg:
    ntpa = (ntpath.basename(ali.text)[:-14])
    print (ntpa)

    mkmeta = open('/home/wcmckee/github/getsdrawnblog/posts/' +  ntpa + '.rst', 'w')

    mkmeta.write('.. |' + ntpa + '| image:: ' + ali.text)
    
    mkmeta.close()
    
    mkmeta = open('/home/wcmckee/github/getsdrawnblog/posts/' + ntpa + '.meta', 'w')

    mkmeta.write(ntpa + '\n' + ntpa + '\n' + str(ardat) + ' ' + str(artim))

    mkmeta.close()
'''   


# In[ ]:




# In[ ]:




# In[225]:

for rsunw in rsunewq:
    #print (rsunw.author)
    #print (rsunw.author)
    mkmeta = open('/home/wcmckee/github/getsdrawnblog/posts/' +  str(rsunw.author) + '.rst', 'w')
    mkmeta.write('.. image:: ' + rsunw.url)
    mkmeta.close()
    
    opmeta = open('/home/wcmckee/github/getsdrawnblog/posts/' + str(rsunw.author) + '.meta', 'w')
    
    opmeta.write((str(rsunw.author) + '\n' + str(rsunw.author) + '\n' + str(ardat) + ' ' + str(artim)))
    
    opmeta.close()


# In[228]:

import os


# In[229]:

os.chdir('/home/wcmckee/github/getsdrawnblog/')


# In[230]:

os.system('nikola build')


# In[ ]:



