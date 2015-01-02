# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h1>GetsDrawn DotCom</h1>

# <markdowncell>

# This is a python script to generate the website GetsDrawn. It takes data from /r/RedditGetsDrawn and makes something awesome.
# 
# The script has envolved and been rewritten several times. 
# 
# The first script for rgdsnatch was written after I got banned from posting my artwork on /r/RedditGetsDrawn. The plan was to create a new site that displayed stuff from /r/RedditGetsDrawn. 
# 
# Currently it only displays the most recent 25 items on redditgetsdrawn.
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
# Extending the subreddits it gets data from to cycle though a list, run script though list of subreddits.

# <codecell>

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

# <codecell>

gtsdrndir = ('/home/wcmckee/getsdrawndotcom')

# <codecell>

os.chdir(gtsdrndir)

# <codecell>

r = praw.Reddit(user_agent='getsdrawndotcom')

# <codecell>

#getmin = r.get_redditor('itwillbemine')

# <codecell>

#mincom = getmin.get_comments()

# <codecell>

#engine = pyttsx.init()

#engine.say('The quick brown fox jumped over the lazy dog.')
#engine.runAndWait()

# <codecell>

#shtweet = []

# <codecell>

#for mi in mincom:
#    print mi
#    shtweet.append(mi)

# <codecell>

bodycom = []
bodyicv = dict()

# <codecell>

#beginz = pyttsx.init()

# <codecell>

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

# <codecell>

#bodycom 

# <codecell>

getnewr = r.get_subreddit('redditgetsdrawn')

# <codecell>

rdnew = getnewr.get_new()

# <codecell>

lisrgc = []
lisauth = []

# <codecell>

for uz in rdnew:
    #print uz
    lisrgc.append(uz)

# <codecell>

gtdrndic = dict()

# <codecell>

imgdir = ('/home/wcmckee/getsdrawndotcom/imgs')

# <codecell>

artlist = os.listdir(imgdir)

# <codecell>

from time import time

# <codecell>

yearz = strftime("%y", gmtime())
monthz = strftime("%m", gmtime())
dayz = strftime("%d", gmtime())


#strftime("%y %m %d", gmtime())


# <codecell>

imgzdir = ('imgs/')
yrzpat = (imgzdir + yearz)
monzpath = (yrzpat + '/' + monthz)
dayzpath = (monzpath + '/' + dayz)
rmgzdays = (dayzpath + '/reference')
imgzdays = (dayzpath + '/art')

repathz = ('imgs/' + yearz + '/' + monthz + '/' + dayz + '/')

# <codecell>


# <codecell>

imgzdays

# <codecell>

repathz

# <codecell>

def ospacheck():
    if os.path.isdir(imgzdir + yearz) == True:
        print 'its true'
    else:
        print 'its false'
        os.mkdir(imgzdir + yearz)
    

# <codecell>

ospacheck()

# <codecell>

#if os.path.isdir(imgzdir + yearz) == True:
#    print 'its true'
#else:
#    print 'its false'
#    os.mkdir(imgzdir + yearz)

# <codecell>

if os.path.isdir(monzpath) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(monzpath)

#os.mkdir(monzpath)

# <codecell>

if os.path.isdir(dayzpath) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(dayzpath)

#os.mkdir(dayzpath)

# <codecell>

if os.path.isdir(imgzdays) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(imgzdays)

# <codecell>

if os.path.isdir(rmgzdays) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(rmgzdays)

# <codecell>

#artlist

# <codecell>

httpad = ('http://getsdrawn.com/imgs')

# <codecell>

#im = Image.new("RGB", (512, 512), "white")
#im.save(file + ".thumbnail", "JPEG")

# <codecell>

for lisr in lisrgc:
    gtdrndic.update({'title': lisr.title})
    lisauth.append(str(lisr.author))

# <codecell>

rmgzdays = (dayzpath + '/reference')
imgzdays = (dayzpath + '/art')

# <codecell>

os.chdir(imgzdays)

# <codecell>

rmgzdays

# <codecell>

#os.listdir(dayzpath)

# <codecell>

for lisa in lisauth:
    #print lisa + '-line.png'
    im = Image.new("RGB", (512, 512), "white")
    im.save(lisa + '-line.png')
    im = Image.new("RGB", (512, 512), "white")
    im.save(lisa + '-bw.png')

    #print lisa + '-bw.png'
    im = Image.new("RGB", (512, 512), "white")
    im.save(lisa + '-colour.png')

    #print lisa + '-colour.png'

# <codecell>

os.listdir('/home/wcmckee/getsdrawndotcom/imgs')

# <codecell>

lisauth

# <markdowncell>

# I want to save the list of usernames that submit images as png files in a dir. 
# Currently when I call the list of authors it returns Redditor(user_name='theusername'). I want to return 'theusername'.
# Once this is resolved I can add '-line.png' '-bw.png' '-colour.png' to each folder. 

# <codecell>

lisr.author

# <codecell>

namlis = []

# <codecell>

opsinz = open('/home/wcmckee/visignsys/index.meta', 'r')
panz = opsinz.read()

# <codecell>

os.chdir('/home/wcmckee/getsdrawndotcom/' + rmgzdays)

# <codecell>

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

# <codecell>

apsize = []

# <codecell>

aptype = []

# <codecell>

basewidth = 600

# <codecell>

imgdict = dict()

# <codecell>

for rmglis in os.listdir('/home/wcmckee/getsdrawndotcom/' + rmgzdays):
    print rmglis
    im = Image.open(rmglis)
    print im.size
    imgdict.update({rmglis : im.size})
    #im.thumbnail(size, Image.ANTIALIAS)
    #im.save(file + ".thumbnail", "JPEG")
    apsize.append(im.size)
    aptype.append(rmglis)

# <codecell>

for imdva in imgdict.values():
    #print imdva
    for deva in imdva:
        #print deva
        if deva < 1000:
            print 'omg less than 1000'
        else:
            print 'omg more than 1000'
            print deva / 2
            #print imgdict.values
            # Needs to update imgdict.values with this new number. Must halve height also.

# <codecell>

#basewidth = 300
#img = Image.open('somepic.jpg')
#wpercent = (basewidth/float(img.size[0]))
#hsize = int((float(img.size[1])*float(wpercent)))
#img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
#img.save('sompic.jpg')

# <codecell>

for numz in apsize:
    print numz[0]
    if numz[0] > 800:
        print ('greater than 800')
    else:
        print ('less than 800!')

# <codecell>

reliz = []

# <codecell>

for refls in os.listdir('/home/wcmckee/getsdrawndotcom/' + rmgzdays):
    #print rmgzdays + refls
    reliz.append(rmgzdays + '/' + refls)

# <codecell>


# <codecell>

reliz

# <codecell>

aptype

# <codecell>

doc = dominate.document(title='GetsDrawn')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type ='text/javascript', src='script.js')
    
    with div():
        attr(cls='header')
        h1('GetsDrawn')
        p(img('imgs/getsdrawn-bw.png', src='imgs/getsdrawn-bw.png'))
        #p(img('imgs/15/01/02/ReptileLover82-reference.png', src= 'imgs/15/01/02/ReptileLover82-reference.png'))
        h1('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        p(panz)
        p(bodycom)
    
    

with doc:
    with div(id='body').add(ol()):
        for rdz in reliz:
            #h1(rdz.title)
            #a(rdz.url)
            #p(img(rdz, src='%s' % rdz))
            print rdz
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

# <codecell>

docre = doc.render()

# <codecell>

#s = docre.decode('ascii', 'ignore')

# <codecell>

yourstring = docre.encode('ascii', 'ignore').decode('ascii')

# <codecell>

indfil = ('/home/wcmckee/getsdrawndotcom/index.html')

# <codecell>

mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()

# <codecell>

#os.system('scp -r /home/wcmckee/getsdrawndotcom/ wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom')

# <codecell>

#rsync -azP source destination

# <codecell>

#updatehtm = raw_input('Update index? Y/n')
#updateref = raw_input('Update reference? Y/n')

#if 'y' or '' in updatehtm:
#    os.system('scp -r /home/wcmckee/getsdrawndotcom/index.html wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/index.html')
#elif 'n' in updatehtm:
#    print 'not uploading'
#if 'y' or '' in updateref:
#    os.system('rsync -azP /home/wcmckee/getsdrawndotcom/ wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/')

# <codecell>

#os.system('scp -r /home/wcmckee/getsdrawndotcom/index.html wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/index.html')

# <codecell>

#os.system('scp -r /home/wcmckee/getsdrawndotcom/style.css wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/style.css')

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


