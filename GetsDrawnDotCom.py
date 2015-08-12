
# coding: utf-8

# <h1>GetsDrawn DotCom</h1>

# This is a python script to generate the website GetsDrawn. It takes data from /r/RedditGetsDrawn and makes something awesome.
# 
# The script has envolved and been rewritten several times. 
# 
# The first script for rgdsnatch was written after I got banned from posting my artwork on /r/RedditGetsDrawn. The plan was to create a new site that displayed stuff from /r/RedditGetsDrawn. 
# 
# Currently it gets the most recent 25 items on redditgetsdrawn, and saves it to a folder.  The script looks at the newest 25 reference photos on RedditGetsDrawn. It focuses only on jpeg/png images and ignores and links to none .jpg or .png ending files. 
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

# In[1]:

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
import getpass
import random
from TwitterFollowBot import TwitterBot


# In[2]:

my_bot = TwitterBot()


# In[3]:

hosnam = getpass.getuser()


# In[4]:

gtsdrndir = ('/home/' + hosnam + '/getsdrawndotcom/')


# In[5]:

gtsdrndir


# In[6]:

if os.path.isdir(gtsdrndir) == True:
    print ('its true')
else:
    print ('its false')
    os.mkdir(gtsdrndir)


# In[7]:

os.chdir(gtsdrndir)


# In[8]:

r = praw.Reddit(user_agent='getsdrawndotcom')


# In[9]:

#getmin = r.get_redditor('itwillbemine')


# In[10]:

#mincom = getmin.get_comments()


# In[11]:

#engine = pyttsx.init()

#engine.say('The quick brown fox jumped over the lazy dog.')
#engine.runAndWait()


# In[12]:

#shtweet = []


# In[13]:

#for mi in mincom:
#    print mi
#    shtweet.append(mi)


# In[14]:

bodycom = []
bodyicv = dict()


# In[15]:

#beginz = pyttsx.init()


# In[16]:

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


# In[17]:

#bodycom 


# In[18]:

getnewr = r.get_subreddit('redditgetsdrawn')


# In[19]:

rdnew = getnewr.get_new()


# In[20]:

lisrgc = []
lisauth = []


# In[21]:

for uz in rdnew:
    #print uz
    lisrgc.append(uz)


# In[22]:

gtdrndic = dict()


# In[23]:

imgdir = (gtsdrndir + 'imgs')


# In[24]:

imgdir


# In[25]:

if os.path.isdir(imgdir) == True:
    print ('its true')
else:
    print ('its false')
    os.mkdir(imgdir)


# In[26]:

artlist = os.listdir(imgdir)


# In[27]:

from time import time


# In[28]:

yearz = strftime("%y", gmtime())
monthz = strftime("%m", gmtime())
dayz = strftime("%d", gmtime())


#strftime("%y %m %d", gmtime())


# In[29]:

yrzpat = (imgdir + '/' + yearz)
monzpath = (yrzpat + '/' + monthz)
dayzpath = (monzpath + '/' + dayz)
rmgzdays = (dayzpath + '/reference')
imgzdays = (dayzpath + '/art')
metzdays = (dayzpath + '/meta')

repathz = (imgdir + '/' + yearz + '/' + monthz + '/' + dayz + '/')


# In[30]:

repathz


# In[31]:

dayzpath


# In[32]:

imgzdays


# In[33]:

repathz


# In[34]:

def ospacheck():
    if os.path.isdir(imgdir + yearz) == True:
        print ('its true')
    else:
        print ('its false')
        os.mkdir(imgdir + yearz)
    


# In[35]:

ospacheck()


# In[36]:

#if os.path.isdir(imgzdir + yearz) == True:
#    print 'its true'
#else:
#    print 'its false'
#    os.mkdir(imgzdir + yearz)


# In[37]:

lizmon = ['monzpath', 'dayzpath', 'imgzdays', 'rmgzdays', 'metzdays']


# Something is wrong with the script and it's no longer creating these dir in the correct folder. How did this break?
# Fixed that but problems with it
# Getting error:
# OSError: [Errno 17] File exists: '/home/wcmckee/getsdrawndotcom/imgs/15/01'
# If the file exists it should be skipping over it, thats why it has the os.path.isdir == True:
#  print its true
# else 
#  print its false, and make the dir

# In[38]:

if os.path.isdir(monzpath) == True:
    print ('its true')
else:
    print ('its false')
    #os.mkdir('/home/wcmckee/getsdrawndotcom/' + monzpath)


# In[39]:

if os.path.isdir(imgzdays) == True:
    print ('its true')
else:
    print ('its false')
    os.mkdir(imgzdays)
    
if os.path.isdir(rmgzdays) == True:
    print ('its true')
else:
    print ('its false')
    os.mkdir(rmgzdays)
    
if os.path.isdir(metzdays) == True:
    print ('its true')
else:
    print ('its false')
    os.mkdir(metzdays)
    
if os.path.isdir(dayzpath) == True:
    print ('its true')
else:
    print ('its false')
    os.mkdir(dayzpath)


# Need to fix dir to just have /imgs/15/02/reference/imgnam-reference.jpg

# In[40]:

monzpath


# In[ ]:




# In[41]:

iwcpath = 'imgs/' + yearz + '/' + monthz + '/' + dayz + '/reference'

#monzpath = (yrzpat + '/' + monthz)
#dayzpath = (monzpath + '/' + dayz)
#rmgzdays = (dayzpath + '/reference')


# In[42]:

#for liz in lizmon:
#    if os.path.isdir(liz) == True:
##        print 'its true'
 #   else:
#        print 'its false'
#        os.mkdir(liz)


# In[43]:

fullhom = ('/home/wcmckee/getsdrawndotcom/')


# In[44]:

#artlist


# In[45]:

httpad = ('http://getsdrawn.com/imgs')


# In[46]:

#im = Image.new("RGB", (512, 512), "white")
#im.save(file + ".thumbnail", "JPEG")


# In[47]:

rmgzdays = (dayzpath + '/reference')
imgzdays = (dayzpath + '/art')
metzdays = (dayzpath + '/meta')


# In[48]:

os.chdir(metzdays)


# In[49]:

metadict = dict()


# if i save the data to the file how am i going to get it to update as the post is archieved. Such as up and down votes. 

# In[50]:

rgde = len(lisrgc)


# In[51]:

rgde


# In[52]:

alrgds = dict()


# In[53]:

#for lisr in lisrgc:
#    print(lisr.author)
#    print(lisr.title[0:30])


# In[54]:

for lisz in lisrgc:
    metadict.update({'up': lisz.ups})
    metadict.update({'down': lisz.downs})
    metadict.update({'title': lisz.title})
    metadict.update({'created': lisz.created})
    
    #metadict.update({'createdutc': lisz.created_utc})
    #print lisz.ups
    #print lisz.downs
    #print lisz.created
    #print lisz.comments


# In[55]:

import random


# In[56]:

ranchor = random.choice(lisrgc)


# In[57]:

titshort = ranchor.title[0:30]


# In[58]:

titsre =titshort.replace(' ', '')


# In[59]:

titsre


# In[60]:

ranchor.url


# In[61]:

ranautr =  (ranchor.author)


# In[62]:

hasra = ('#') + str(ranautr)


# In[63]:

hasra


# In[64]:

hasgd = ('#getsdrawn')


# In[ ]:




# In[ ]:




# In[ ]:




# In[65]:

urlfin = ('http://getsdrawn.com/' + iwcpath + '/' + str(ranautr) + '-reference.png')


# In[66]:

(urlfin)


# In[67]:

twez = (titsre + ' ' + urlfin + ' ' + hasra + ' ' + hasgd)


# In[68]:

len(twez)


# In[ ]:




# Need to save json object.
# 
# Dict is created but it isnt saving. Looping through lisrgc twice, should only require the one loop.
# 
# Cycle through lisr and append to dict/concert to json, and also cycle through lisr.author meta folders saving the json that was created. 

# In[69]:

for lisr in lisrgc:
    gtdrndic.update({'title': lisr.title})
    lisauth.append(str(lisr.author))
    for osliz in os.listdir(metzdays):
        with open(str(lisr.author) + '.meta', "w") as f:
            rstrin = lisr.title.encode('ascii', 'ignore').decode('ascii')
            #print matdict
            #metadict = dict()
            #for lisz in lisrgc:
            #    metadict.update({'up': lisz.ups})
            #    metadict.update({'down': lisz.downs})
            #    metadict.update({'title': lisz.title})
            #    metadict.update({'created': lisz.created})
            f.write(rstrin)


# In[70]:

#matdict


# I have it creating a meta folder and creating/writing username.meta files. It wrote 'test' in each folder, but now it writes the photo author title of post.. the username/image data. It should be writing more than author title - maybe upvotes/downvotes, subreddit, time published etc.
# 

# In[71]:

#os.listdir(dayzpath)


# Instead of creating these white images, why not download the art replies of the reference photo.

# In[72]:

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


# In[73]:

#lisauth


# I want to save the list of usernames that submit images as png files in a dir. 
# Currently when I call the list of authors it returns Redditor(user_name='theusername'). I want to return 'theusername'.
# Once this is resolved I can add '-line.png' '-bw.png' '-colour.png' to each folder. 

# In[74]:

#lisr.author


# In[75]:

namlis = []


# In[76]:

#opsinz = open('/home/wcmckee/visignsys/index.meta', 'r')
#panz = opsinz.read()


# In[77]:

os.chdir(rmgzdays)


# Filter the non jpeg/png links. Need to perform request or imgur api to get the jpeg/png files from the link. Hey maybe bs4?

# In[ ]:




# In[78]:

#from imgurpython import ImgurClient


# In[79]:

#opps = open('/home/wcmckee/ps.txt', 'r')
#opzs = open('/home/wcmckee/ps2.txt', 'r')
#oprd = opps.read()
#opzrd = opzs.read()


# In[80]:

#client = ImgurClient(oprd, opzrd)

# Example request
#items = client.gallery()
#for item in items:
#    print(item.link)
    

#itz = client.get_album_images()


# In[81]:

#galim = client.get_image('SBaV275')


# In[82]:

#galim.size


# In[83]:

#gelim = client.get_album_images('LTDJ9')


# In[84]:

#gelim


# In[85]:

#from urlparse import urlparse


# In[86]:

#linklis = []


# I need to get the image ids from each url. Strip the http://imgur.com/ from the string. The gallery id is the random characters after. if it's an album a is added. if multi imgs then , is used to seprate. 
# 
# Doesnt currently work. 
# 
# Having problems with mixed /a/etwet and wetfwet urls. Using .strip('/') to remove forward slash in front of path. 

# In[87]:

#pathlis = []


# In[88]:

#for rdz in lisrgc:
#    if 'http://imgur.com/' in rdz.url:
#        print rdz.url
#        parsed = urlparse(rdz.url)
##        print parsed.path.strip('/')
 #       pathlis.append(parsed.path.strip('/'))
        #for pared in parsed.path:
        #    print pared.strip('/')
        #itgar = client.gallery_item(parsed.path.strip('/'))
        #itz = client.get_album_images(parsed.path.strip('a/'))
#        reimg = requests.get(rdz.url)
##        retxt = reimg.text
#        souptxt = BeautifulSoup(''.join(retxt))
#        soupurz = souptxt.findAll('img')
#        for soupuz in soupurz:
#            imgurl = soupuz['src']
#            print imgurl
#            linklis.append(imgurl)
            
            #try:
            #    imzdata = requests.get(imgurl)


# In[89]:

#pathlis


# In[90]:

#noalis = []


# In[91]:

#for pathl in pathlis:
#    if 'a/' in pathl:
#        print 'a found'
#    else:
#        noalis.append(pathl)


# In[92]:

#if 'a/' in pathlis:
#    print 'a found'
#else:
#    noalis.append(pathlis)


# In[93]:

#for noaz in noalis:
#    print noaz
    #itgar = client.gallery_item()


# In[94]:

#linklis


# In[95]:

#if '.jpg' in linklis:
#    print 'yes'
#else:
#    print 'no'


# In[96]:

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


# In[97]:

apsize = []


# In[98]:

aptype = []


# In[99]:

basewidth = 600


# In[100]:

imgdict = dict()


# In[101]:

for rmglis in os.listdir(rmgzdays):
    #print rmglis
    im = Image.open(rmglis)
    #print im.size
    imgdict.update({rmglis : im.size})
    #im.thumbnail(size, Image.ANTIALIAS)
    #im.save(file + ".thumbnail", "JPEG")
    apsize.append(im.size)
    aptype.append(rmglis)


# In[102]:

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


# In[103]:

#basewidth = 300
#img = Image.open('somepic.jpg')
#wpercent = (basewidth/float(img.size[0]))
#hsize = int((float(img.size[1])*float(wpercent)))
#img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
#img.save('sompic.jpg')


# In[104]:

#os.chdir(metzdays)


# In[ ]:




# In[105]:

#for numz in apsize:
#    print numz[0]
 #   if numz[0] > 800:
#        print ('greater than 800')
#    else:
#        print ('less than 800!')


# In[106]:

reliz = []


# In[107]:

for refls in os.listdir(rmgzdays):
    #print rmgzdays + refls
    reliz.append(iwcpath + '/' + refls)


# In[108]:

len(reliz)


# Tweet each reference img in list, removing the item when it's tweeted so that same item isn't tweeted twice. 
# Make new list of items to tweet, appending in new items when site is updated

# In[109]:

for apt in aptype:
    print (apt)


# In[ ]:




# In[ ]:




# In[110]:

#opad = open('/home/wcmckee/ad.html', 'r')


# In[111]:

#opred = opad.read()


# In[112]:

#str2 = opred.replace("\n", "")


# In[113]:

#str2


# In[ ]:




# In[114]:

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
        a('https://github.com/getsdrawn/getsdrawndotcom')
        a('https://reddit.com/r/redditgetsdrawn')

#print doc


# In[115]:

docre = doc.render()
#s = docre.decode('ascii', 'ignore')
yourstring = docre.encode('ascii', 'ignore').decode('ascii')
indfil = ('/home/wcmckee/getsdrawndotcom/index.html')
mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()


# In[116]:

mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()


# In[110]:

#os.system('scp -r /home/wcmckee/getsdrawndotcom/ wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom')


# In[111]:

#rsync -azP source destination


# In[112]:

#updatehtm = raw_input('Update index? Y/n')
#updateref = raw_input('Update reference? Y/n')

#if 'y' or '' in updatehtm:
#    os.system('scp -r /home/wcmckee/getsdrawndotcom/index.html wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/index.html')
#elif 'n' in updatehtm:
#    print 'not uploading'
#if 'y' or '' in updateref:
#    os.system('rsync -azP /home/wcmckee/getsdrawndotcom/ wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/')


# In[113]:

#os.system('scp -r /home/wcmckee/getsdrawndotcom/index.html wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/index.html')


# In[105]:

#os.system('scp -r /home/wcmckee/getsdrawndotcom/style.css wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/style.css')


# In[118]:

my_bot.send_tweet(twez)


# In[ ]:




# In[321]:




# In[138]:




# In[138]:




# In[ ]:



