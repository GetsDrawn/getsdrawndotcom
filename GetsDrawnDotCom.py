
# coding: utf-8

# <h1>GetsDrawn DotCom</h1>

# This is a python script to generate the website GetsDrawn. It takes data from /r/RedditGetsDrawn and makes something awesome.
# 
# The script has envolved and been rewritten several times. 
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

# Work on 

# In[2]:

import os 
import requests
from bs4 import BeautifulSoup
import re
import json
import time
import praw
import dominate
from dominate.tags import * 
from time import gmtime, strftime
#import nose
#import unittest
import numpy as np
import pandas as pd
from pandas import *
from PIL import Image
from pprint import pprint
#import pyttsx
import shutil

import arrow


# In[3]:

gtsdrndir = ('/home/wcmckee/getsdrawndotcom')


# In[4]:

os.chdir(gtsdrndir)


# In[5]:

r = praw.Reddit(user_agent='getsdrawndotcom')


# In[6]:

#getmin = r.get_redditor('itwillbemine')


# In[7]:

#mincom = getmin.get_comments()


# In[8]:

#engine = pyttsx.init()

#engine.say('The quick brown fox jumped over the lazy dog.')
#engine.runAndWait()


# In[9]:

#shtweet = []


# In[10]:

#for mi in mincom:
#    print mi
#    shtweet.append(mi)


# In[11]:

bodycom = []
bodyicv = dict()


# In[12]:

#beginz = pyttsx.init()


# In[13]:

#for shtz in shtweet:
#    print shtz.downs
#    print shtz.ups
#    print shtz.body
#    print shtz.replies
    #beginz.say(shtz.author)
    #beginz.say(shtz.body)
    #beginz.runAndWait()
    
#    bodycom.append(shtz.body)
    #bodyic


# In[14]:

#bodycom 


# In[15]:

getnewr = r.get_subreddit('redditgetsdrawnbadly')


# In[16]:

rdnew = getnewr.get_new()


# In[17]:

lisrgc = []
lisauth = []


# In[18]:

for uz in rdnew:
    #print uz
    lisrgc.append(uz)


# In[19]:

gtdrndic = dict()


# In[20]:

imgdir = ('/home/wcmckee/getsdrawndotcom/imgs')


# In[21]:

artlist = os.listdir(imgdir)


# In[22]:

from time import time


# In[23]:

yearz = strftime("%y", gmtime())
monthz = strftime("%m", gmtime())
dayz = strftime("%d", gmtime())


#strftime("%y %m %d", gmtime())



# In[24]:

imgzdir = ('imgs/')
yrzpat = (imgzdir + yearz)
monzpath = (yrzpat + '/' + monthz)
dayzpath = (monzpath + '/' + dayz)
rmgzdays = (dayzpath + '/reference')
imgzdays = (dayzpath + '/art')
metzdays = (dayzpath + '/meta')

repathz = ('imgs/' + yearz + '/' + monthz + '/' + dayz + '/')


# In[25]:

metzdays


# In[26]:

imgzdays


# In[27]:

repathz


# In[28]:

def ospacheck():
    if os.path.isdir(imgzdir + yearz) == True:
        print 'its true'
    else:
        print 'its false'
        os.mkdir(imgzdir + yearz)
    


# In[29]:

ospacheck()


# In[30]:

#if os.path.isdir(imgzdir + yearz) == True:
#    print 'its true'
#else:
#    print 'its false'
#    os.mkdir(imgzdir + yearz)


# In[31]:

if os.path.isdir(monzpath) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(monzpath)

#os.mkdir(monzpath)


# In[32]:

if os.path.isdir(dayzpath) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(dayzpath)

#os.mkdir(dayzpath)


# In[33]:

if os.path.isdir(imgzdays) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(imgzdays)


# In[34]:

if os.path.isdir(rmgzdays) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(rmgzdays)


# In[35]:

if os.path.isdir(metzdays)  == True:
    print 'its true'
else:
    print 'its failse'
    os.mkdir(metzdays)


# In[36]:

fullhom = ('/home/wcmckee/getsdrawndotcom/')


# In[37]:

os.listdir(fullhom + metzdays)


# In[38]:

#artlist


# In[39]:

httpad = ('http://getsdrawn.com/imgs')


# In[40]:

#im = Image.new("RGB", (512, 512), "white")
#im.save(file + ".thumbnail", "JPEG")


# In[41]:

rmgzdays = (dayzpath + '/reference')
imgzdays = (dayzpath + '/art')
metzdays = (dayzpath + '/meta')


# In[42]:

os.chdir(fullhom + metzdays)


# In[43]:

for lisr in lisrgc:
    gtdrndic.update({'title': lisr.title})
    lisauth.append(str(lisr.author))
    for osliz in os.listdir(fullhom + metzdays):
        with open(str(lisr.author) + '.meta', "w") as f:
            rstrin = lisr.title.encode('ascii', 'ignore').decode('ascii')
            f.write(rstrin)


# I have it creating a meta folder and creating/writing username.meta files. It wrote 'test' in each folder, but now it writes the photo author title of post.. the username/image data. 

# In[44]:

#os.listdir(dayzpath)


# Instead of creating these white images, why not download the art replies of the reference photo.

# In[45]:

#for lisa in lisauth:
#    #print lisa + '-line.png'
#    im = Image.new("RGB", (512, 512), "white")
#    im.save(lisa + '-line.png')
#    im = Image.new("RGB", (512, 512), "white")
#    im.save(lisa + '-bw.png')

    #print lisa + '-bw.png'
#    im = Image.new("RGB", (512, 512), "white")
#    im.save(lisa + '-colour.png')

    #print lisa + '-colour.png'


# In[46]:

os.listdir('/home/wcmckee/getsdrawndotcom/imgs')


# In[47]:

#lisauth


# I want to save the list of usernames that submit images as png files in a dir. 
# Currently when I call the list of authors it returns Redditor(user_name='theusername'). I want to return 'theusername'.
# Once this is resolved I can add '-line.png' '-bw.png' '-colour.png' to each folder. 

# In[48]:

#lisr.author


# In[49]:

namlis = []


# In[52]:

#opsinz = open('/home/wcmckee/visignsys/index.meta', 'r')
#panz = opsinz.read()


# In[53]:

os.chdir('/home/wcmckee/getsdrawndotcom/' + rmgzdays)


# In[83]:

#panz()
for rdz in lisrgc:
    (rdz.title)
    #a(rdz.url)
    if 'http://i.imgur.com' in rdz.url:
        #print rdz.url
        print (rdz.url)
        url = rdz.url
        response = requests.get(url, stream=True)
        with open(str(rdz.author) + '-reference.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            del response


# In[55]:

apsize = []


# In[56]:

aptype = []


# In[57]:

basewidth = 600


# In[58]:

imgdict = dict()


# In[79]:

rmgzdays


# In[76]:

for rmglis in os.listdir('/home/wcmckee/getsdrawndotcom/' + rmgzdays):
    #print rmglis
    im = Image.open(rmglis)
    #print im.size
    imgdict.update({rmglis : im.size})
    #imgdict.update({rmglis : im.getcolors()})
    #im.thumbnail(size, Image.ANTIALIAS)
    #im.save(file + ".thumbnail", "JPEG")
    apsize.append(im.size)
    aptype.append(rmglis)


# In[77]:

imgdict


# In[60]:

#for imdva in imgdict.values():
    #print imdva
    #for deva in imdva:
        #print deva
     #   if deva < 1000:
      #      print 'omg less than 1000'
       # else:
        #    print 'omg more than 1000'
         #   print deva / 2
            #print imgdict.values
            # Needs to update imgdict.values with this new number. Must halve height also.


# In[61]:

#basewidth = 300
#img = Image.open('somepic.jpg')
#wpercent = (basewidth/float(img.size[0]))
#hsize = int((float(img.size[1])*float(wpercent)))
#img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
#img.save('sompic.jpg')


# In[62]:

#os.chdir(metzdays)


# In[62]:




# In[63]:

#for numz in apsize:
#    print numz[0]
 #   if numz[0] > 800:
#        print ('greater than 800')
#    else:
#        print ('less than 800!')


# In[64]:

reliz = []


# In[65]:

for refls in os.listdir('/home/wcmckee/getsdrawndotcom/' + rmgzdays):
    #print rmgzdays + refls
    reliz.append(rmgzdays + '/' + refls)


# In[144]:

#reliz


# In[145]:

#aptype


# In[147]:

#opad = open('/home/wcmckee/ad.html', 'r')


# In[149]:

#opred = opad.read()


# In[150]:

#str2 = opred.replace("\n", "")


# In[151]:

#str2


# In[153]:

doc = dominate.document(title='GetsDrawn')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type ='text/javascript', src='script.js')
    #str(str2)
    
    with div():
        attr(cls='header')
        h1('GetsDrawn')
        p(img('imgs/getsdrawn-bw.png', src='imgs/getsdrawn-bw.png'))
        #p(img('imgs/15/01/02/ReptileLover82-reference.png', src= 'imgs/15/01/02/ReptileLover82-reference.png'))
        h1('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        #p(panz)
        p(bodycom)
    
    

with doc:
    with div(id='body').add(ol()):
        for rdz in reliz:
            #h1(rdz.title)
            #a(rdz.url)
            #p(img(rdz, src='%s' % rdz))
            #print rdz
            p(img(rdz, src = rdz))
            p(rdz)


                
            #print rdz.url
            #if '.jpg' in rdz.url:
            #    img(rdz.urlz)
            #else:
            #    a(rdz.urlz)
            #h1(str(rdz.author))
            
            #li(img(i.lower(), src='%s' % i))

    with div():
        attr(cls='body')
        p('GetsDrawn is open source')
        a('https://github.com/wcmckee/wcmckee')
        a('https://reddit.com/r/redditgetsdrawn')

#print doc


# In[154]:

docre = doc.render()


# In[155]:

#s = docre.decode('ascii', 'ignore')


# In[156]:

yourstring = docre.encode('ascii', 'ignore').decode('ascii')


# In[157]:

indfil = ('/home/wcmckee/getsdrawndotcom/index.html')


# In[158]:

mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()


# In[ ]:

#os.system('scp -r /home/wcmckee/getsdrawndotcom/ wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom')


# In[ ]:

#rsync -azP source destination


# In[ ]:

#updatehtm = raw_input('Update index? Y/n')
#updateref = raw_input('Update reference? Y/n')

#if 'y' or '' in updatehtm:
#    os.system('scp -r /home/wcmckee/getsdrawndotcom/index.html wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/index.html')
#elif 'n' in updatehtm:
#    print 'not uploading'
#if 'y' or '' in updateref:
#    os.system('rsync -azP /home/wcmckee/getsdrawndotcom/ wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/')


# In[ ]:

#os.system('scp -r /home/wcmckee/getsdrawndotcom/index.html wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/index.html')


# In[ ]:

#os.system('scp -r /home/wcmckee/getsdrawndotcom/style.css wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/style.css')


# In[88]:

#os.system("find /home/wcmckee/getsdrawndotcom/ -type f -name '*-reference.png'")


# In[97]:

lisfed = []


# In[191]:

for oswalk in os.walk('/home/wcmckee/getsdrawndotcom/'):
    #if '*-reference.png' in oswalk:
    #print oswalk
    lisfed.append(oswalk)


# In[192]:

oswalk


# In[106]:

getdrndir = ('/home/wcmckee/getsdrawndotcom/')


# In[107]:

import walkdir 


# In[112]:

for filz in walkdir.filtered_walk(getdrndir,  included_dirs='*-reference.png'):
    print filz


# In[116]:

walkz = ('/home/wcmckee/getsdrawndotcom/')


# In[117]:

walkz


# In[137]:

refim = []


# In[140]:

from walkdir import filtered_walk, dir_paths, all_paths, file_paths

files = file_paths(filtered_walk('/home/wcmckee/getsdrawndotcom/', depth=100, included_files=['*-reference.png']))


# In[159]:

for fil in files:
    #print fil
    refim.append(fil)


# In[160]:

len(refim)


# In[165]:

nalis = []


# In[180]:

for ref in refim:
    #print ref[54:-14]
    nalis.append(ref[54:-14])
#54


# In[169]:

nalis.sort()


# In[171]:

len(nalis)


# In[178]:

filnalis = filter(None, nalis)


# Working good at extracting usernames from folders. Need to look up usernames on reddit. 

# In[189]:

#for filna in filnalis:
#    usrz = r.get_redditor(filna)


# In[190]:

for filn in filnalis:
    print filn


# In[183]:

docall = dominate.document(title='GetsDrawnAll')

with docall.head:
    link(rel='stylesheet', href='style.css')
    script(type ='text/javascript', src='script.js')
    #str(str2)
    
    with div():
        attr(cls='header')
        h1('GetsDrawnAll')
        p(img('imgs/getsdrawn-bw.png', src='imgs/getsdrawn-bw.png'))
        #p(img('imgs/15/01/02/ReptileLover82-reference.png', src= 'imgs/15/01/02/ReptileLover82-reference.png'))
        h1('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        #p(panz)
        p(bodycom)
    
    

with docall:
    with div(id='body').add(ol()):
        for refz in refim:
            #h1(rdz.title)
            #a(rdz.url)
            #p(img(rdz, src='%s' % rdz))
            #print rdz
            p(img(refz, src = refz))
            p(refz)


                
            #print rdz.url
            #if '.jpg' in rdz.url:
            #    img(rdz.urlz)
            #else:
            #    a(rdz.urlz)
            #h1(str(rdz.author))
            
            #li(img(i.lower(), src='%s' % i))

    with div():
        attr(cls='body')
        p('GetsDrawn is open source')
        a('https://github.com/wcmckee/wcmckee')
        a('https://reddit.com/r/redditgetsdrawn')

#print doc


# In[184]:

doctea = docall.render()


# In[185]:

strng = doctea.encode('ascii', 'ignore').decode('ascii')


# In[186]:

getdall = ('/home/wcmckee/getsdrawnall/index.html')


# In[188]:

msav = open(getdall, 'w')
msav.write(strng)
msav.close()


# In[ ]:



