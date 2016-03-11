
# coding: utf-8

# <h1>Nikola GetsDrawn</h1>

# This is a python script to generate the website GetsDrawn. It takes data from /r/RedditGetsDrawn and makes something awesome. It uses the Nikola web framework in to make a website that is mobile friendly. 
# 
# The script has been rewritten several times and developed over time 
# 
# The first script for rgdsnatch was written after I got banned from posting my artwork on /r/RedditGetsDrawn. The plan was to create a new site that displayed stuff from /r/RedditGetsDrawn. 
# 
# Currently it only displays the most recent 25 items on redditgetsdrawn. The script looks at the newest 25 reference photos on RedditGetsDrawn. It focuses only on jpeg/png images and ignores and links to none .jpg or .png ending files. 
# It is needed to instead of ignoring them files - get the image or images in some cases, from the link.
# The photos are always submitted from imgur.
# Still filter out the i.imgur files, but take the links and filter them through a python imgur module returning the .jpeg or .png files. 
# 
# 
# This is moving forward from rgdsnatch.py because I am stuck on it.  
# 
# TODO
# 
# Fix the links that don't link to png/jpeg and link to webaddress. 
# Needs to get the images that are at that web address and embed them.
# 
# Display artwork submitted under the images. 
# 
# Upload artwork to user. Sends them a message on redditgetsdrawn with links. 
# 
# More pandas
# 
# Saves reference images to imgs/year/month/day/reference/username-reference.png
# 
# Saves art images to imgs/year/month/day/art/username-line-bw-colour.png 
# 
# Creates index.html file with:
# Title of site and logo: GetsDrawn
# Last updated date and time. 
# 
# Path of image file /imgs/year/month/day/username-reference.png. 
# (This needs changed to just their username).
# 
# Save off .meta data from reddit of each photo, saving it to reference folder.
# username-yrmnthday.meta - contains info such as author, title, upvotes, downvotes.
# Currently saving .meta files to a meta folder - along side art and reference. 
# 
# Folder sorting system of files. 
# websitename/index.html-style.css-imgs/YEAR(15)-MONTH(2)-DAY(4)/art-reference-meta
# Inside art folder
# Currently it generates USERNAME-line/bw/colour.png 50/50 white files. Maybe should be getting art replies from reddit?
# 
# Inside reference folder
# Reference fold is working decent. 
# it creates USERNAME-reference.png / jpeg files. 
# 
# Currently saves username-line-bw-colour.png to imgs folder. Instead get it to save to imgs/year/month/day/usernames.png.
# Script checks the year/month/day and if folder isnt created, it creates it. If folder is there, exit. 
# Maybe get the reference image and save it with the line/bw/color.pngs
# 
# The script now filters the jpeg and png image and skips links to imgur pages. This needs to be fixed by getting the images from the imgur pages.
# It renames the image files to the redditor username followed by a -reference tag (and ending with png of course).
# It opens these files up with PIL and checks the sizes. 
# It needs to resize the images that are larger than 800px to 800px.
# These images need to be linked in the index.html instead of the imgur altenatives. 
# 
# Instead of the jpeg/png files on imgur they are downloaded to the server with this script. 
# 
# Filter through as images are getting downloaded and if it has been less than certain time or if the image has been submitted before 
# 
# Extending the subreddits it gets data from to cycle though a list, run script though list of subreddits.
# 
# Browse certain days - Current day by default but option to scroll through other days.
# 
# Filters - male/female/animals/couples etc
# Function that returns only male portraits. 
# tags to add to photos. 
# Filter images with tags
# 
# 
# 

# In[3]:

import os 
import requests
from bs4 import BeautifulSoup
import re
import json
import time
import praw
from time import gmtime, strftime
#import nose
#import unittest
#import numpy as np
#import pandas as pd
#from pandas import *
#from PIL import Image
#from pprint import pprint
#import pyttsx
import shutil

import getpass


# In[4]:

myusr = getpass.getuser()


# In[5]:

gtsdrndir = ('/home/' + myusr + '/getsdrawn/')


# In[7]:

os.chdir(gtsdrndir)


# In[8]:

r = praw.Reddit(user_agent='getsdrawndotcom')


# In[9]:

bodycom = []
bodyicv = dict()


# In[10]:

#beginz = pyttsx.init()


# In[11]:

#bodycom 


# In[12]:

getnewr = r.get_subreddit('redditgetsdrawn')


# In[13]:

rdnew = getnewr.get_new()


# In[14]:

lisrgc = []
lisauth = []


# In[15]:

for uz in rdnew:
    #print uz
    lisrgc.append(uz)


# In[16]:

gtdrndic = dict()


# In[17]:

imgdir = ('/home/' + myusr + '/getsdrawn/galleries/')


# In[19]:

artlist = os.listdir(imgdir)


# In[20]:

from time import time


# In[21]:

yearz = strftime("%y", gmtime())
monthz = strftime("%m", gmtime())
dayz = strftime("%d", gmtime())


#strftime("%y %m %d", gmtime())



# In[22]:

#imgzdir = ('')
yrzpat = (imgdir + yearz)
monzpath = (yrzpat + '/' + monthz)
dayzpath = (monzpath + '/' + dayz)
#rmgzdays = (dayzpath + '/reference')
#imgzdays = (dayzpath + '/art')
#metzdays = (dayzpath + '/meta')

repathz = (imgdir + yearz + '/' + monthz + '/' + dayz + '/')


# In[23]:

fulyr = yearz + '-' + monthz + '-' + dayz + '-reference'


# In[24]:

dateful = yearz + '/' + monthz + '/' + dayz


# In[25]:

def ospacheck():
    if os.path.isdir(imgdir + yearz) == True:
        print ('its true')
    else:
        print ('its false')
        os.mkdir(imgdir + yearz)
    


# In[26]:

ospacheck()


# In[27]:

#if os.path.isdir(imgzdir + yearz) == True:
#    print 'its true'
#else:
#    print 'its false'
#    os.mkdir(imgzdir + yearz)


# In[28]:

if os.path.isdir(monzpath) == True:
    print ('its true')
else:
    print ('its false')
    os.mkdir(monzpath)

#os.mkdir(monzpath)


# In[29]:

if os.path.isdir(dayzpath) == True:
    print ('its true')
else:
    print ('its false')
    os.mkdir(dayzpath)

#os.mkdir(dayzpath)


# In[30]:

rmgzdays = (dayzpath + '/reference')
#imgzdays = (dayzpath + '/art')
#metzdays = (dayzpath + '/meta')


# Instead of creating these white images, why not download the art replies of the reference photo.

# I want to save the list of usernames that submit images as png files in a dir. 
# Currently when I call the list of authors it returns Redditor(user_name='theusername'). I want to return 'theusername'.
# Once this is resolved I can add '-line.png' '-bw.png' '-colour.png' to each folder. 

# In[122]:

namlis = []


# In[123]:

#opsinz = open('/home/wcmckee/visignsys/index.meta', 'r')
#panz = opsinz.read()


# In[138]:

oppost = open('/home/' + myusr + '/getsdrawn/posts/' + fulyr + '.md', 'w')


# In[139]:

galpath = ('/galleries/' + dateful + '/')


# In[140]:

#for rdz in lisrgc:
#    print(rdz.thumbnail)
#    print(rdz.title)
#    for rdcom in (rdz.comments):
#        print (rdcom)
#        print(rdcom.author)


# In[143]:

for rdz in lisrgc:
    print(rdz.thumbnail)
    print(rdz.title)
    #print(rdz.author)
    urlthumb = rdz.thumbnail
    response = requests.get(urlthumb, stream=True)
    with open(repathz + str(rdz.author) + '-reference-thumb.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        del response
    #oppost.write(('!' + '[' + toda.strip('.jpg') + '](' + galpath + toda + ')\n\n' + '[' + toda.strip('-reference.jpg') + ']' + '(https://reddit.com/u/' + toda.strip('-reference.jpg') + ')' + '\n\n'))
    #print(rdz.title + '\n![' + str(rdz.author) + '](' + galpath + str(rdz.author) + '-reference-thumb.jpg)\n\n[' + str(rdz.author) + '](https://reddit.com/u/' + str(rdz.author) + ')\n\n')
    oppost.write(('**' + rdz.title + '**\n\n![' + str(rdz.author) + '](' + galpath + str(rdz.author) + '-reference-thumb.jpg)\n\n[' + str(rdz.author) + '](https://reddit.com/u/' + str(rdz.author) + ')\n\n'))
    for rdcom in (rdz.comments):
        print (rdcom)
        print(rdcom.author)
        oppost.write('\n\n' + str(rdcom) + '\n\n' + str(rdcom.author) + '\n\n')


# In[144]:

oppost.close()


# In[145]:

fultdaz = dayz + '/' + monthz + '/' +strftime('%Y')


# In[146]:

oppost.close()


# In[147]:

rstme = ('.. title: ' + fulyr + ' \n' + '.. slug: ' + fulyr+ ' \n' + '.. date: ' + fultdaz)


# In[148]:

opmeta = open('/home/' + myusr + '/getsdrawn/posts/' + fulyr + '.meta', 'w')


# In[149]:

opmeta.write(rstme)


# In[150]:

opmeta.close()


# In[151]:

os.chdir('/home/' + myusr + '/getsdrawn')


# In[ ]:

os.system('nikola build')


# In[ ]:




# In[ ]:



