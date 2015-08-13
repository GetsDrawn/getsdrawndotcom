
# coding: utf-8

# make rst
# 
# Create GetsDrawn post of images

# In[2]:

import requests
import bs4
import json
import arrow
import praw
import os

import ntpath


# In[3]:

r = praw.Reddit(user_agent='getsdrawndotcom')


# In[4]:

rsubred = r.get_subreddit('redditgetsdrawn')


# In[5]:

rsunewq = rsubred.get_new()


# In[6]:

#for rsubcom in rsubred.get_comments():
#    print (rsubcom)
    #if (rsubcom.author) != 'ItWillBeMine':
    #    print (rsubcom)
    #    print (rsubcom.author)
    
    #answer != 'hi':   # not equal
    #   print "no hi"
    #print (rsubcom.author)


# In[7]:

arnowz = arrow.now()


# In[8]:

ardat = arnowz.date()


# In[9]:

str(ardat)


# In[10]:

artim = arnowz.time()


# In[11]:

regetd = requests.get('http://getsdrawn.com')


# In[12]:

#requgetdrn = open('/home/wcmckee/getsdrawndotcom/index.html', 'r')


# In[13]:

bst = bs4.BeautifulSoup(regetd.text)


# In[49]:

bst


# In[14]:

#requgetdrn.close()


# In[ ]:

bst.find('a')


# In[21]:

alimg = bst.find_all('a')
    #print(bs)


# In[92]:

alinkl = list()


# In[93]:

namref = list()


# In[97]:

import ntpath


# In[ ]:




# In[101]:

for ali in alimg:
    ntpa = (ntpath.basename(ali.attrs['href'][:-14]))
    print (ntpa)
    urlink = (ali.attrs['href'])
    #print (ali.attrs['href'])
    alinkl.append((ali.attrs['href']))
    namref.append((ali.attrs['href'][:-4]))
    
    
    mkmeta = open('/home/wcmckee/github/getsdrawnblog/posts/' +  ntpa + '.rst', 'w')
    mkmeta.write('.. image:: ' + urlink)
    mkmeta.close()
    
    opmeta = open('/home/wcmckee/github/getsdrawnblog/posts/' + ntpa + '.meta', 'w')
    
    opmeta.write((ntpa + '\n' + ntpa + '\n' + str(ardat) + ' ' + str(artim)))
    
    #opmeta.close()
    
    #print(ali.text)


# In[ ]:

ntpa = (ntpath.basename(ali.text)[:-14])
print (ntpa)


# In[91]:

namref


# In[ ]:




# In[ ]:

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

for rsunw in rsunewq:
    #print (rsunw.author)
    #print (rsunw.author)
    mkmeta = open('/home/wcmckee/github/getsdrawnblog/posts/' +  str(rsunw.author) + '.rst', 'w')
    mkmeta.write('.. image:: ' + rsunw.url)
    mkmeta.close()
    
    opmeta = open('/home/wcmckee/github/getsdrawnblog/posts/' + str(rsunw.author) + '.meta', 'w')
    
    opmeta.write((str(rsunw.author) + '\n' + str(rsunw.author) + '\n' + str(ardat) + ' ' + str(artim)))
    
    opmeta.close()


# In[15]:

import os


# In[16]:

os.chdir('/home/wcmckee/github/getsdrawnblog/')


# In[17]:

os.system('nikola build')


# In[ ]:



