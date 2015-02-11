
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

# Now saves an html page with all images embed. 
# 
# Create Nikola blog from each post. 

# In[252]:




# In[252]:




# In[253]:

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


# In[254]:

gtsdrndir = ('/home/wcmckee/getsdrawndotcom')


# In[255]:

os.chdir(gtsdrndir)


# In[256]:

r = praw.Reddit(user_agent='getsdrawndotcom')


# In[257]:

#getmin = r.get_redditor('itwillbemine')


# In[258]:

#mincom = getmin.get_comments()


# In[259]:

#engine = pyttsx.init()

#engine.say('The quick brown fox jumped over the lazy dog.')
#engine.runAndWait()


# In[260]:

#shtweet = []


# In[261]:

#for mi in mincom:
#    print mi
#    shtweet.append(mi)


# In[262]:

bodycom = []
bodyicv = dict()


# In[263]:

#beginz = pyttsx.init()


# In[264]:

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


# In[265]:

#bodycom 


# In[266]:

getnewr = r.get_subreddit('redditgetsdrawn')


# In[267]:

rdnew = getnewr.get_new()


# In[268]:

lisrgc = []
lisauth = []


# In[269]:

for uz in rdnew:
    #print uz
    lisrgc.append(uz)


# In[270]:

gtdrndic = dict()


# In[271]:

imgdir = ('/home/wcmckee/getsdrawndotcom/imgs')


# In[272]:

artlist = os.listdir(imgdir)


# In[273]:

from time import time


# In[274]:

yearz = strftime("%y", gmtime())
monthz = strftime("%m", gmtime())
dayz = strftime("%d", gmtime())


#strftime("%y %m %d", gmtime())



# In[275]:

imgzdir = ('imgs/')
yrzpat = (imgzdir + yearz)
monzpath = (yrzpat + '/' + monthz)
dayzpath = (monzpath + '/' + dayz)
rmgzdays = (dayzpath + '/reference')
imgzdays = (dayzpath + '/art')
metzdays = (dayzpath + '/meta')

repathz = ('imgs/' + yearz + '/' + monthz + '/' + dayz + '/')


# In[276]:

metzdays


# In[277]:

imgzdays


# In[278]:

repathz


# In[279]:

def ospacheck():
    if os.path.isdir(imgzdir + yearz) == True:
        print 'its true'
    else:
        print 'its false'
        os.mkdir(imgzdir + yearz)
    


# In[280]:

ospacheck()


# In[281]:

#if os.path.isdir(imgzdir + yearz) == True:
#    print 'its true'
#else:
#    print 'its false'
#    os.mkdir(imgzdir + yearz)


# In[282]:

if os.path.isdir(monzpath) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(monzpath)

#os.mkdir(monzpath)


# In[283]:

if os.path.isdir(dayzpath) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(dayzpath)

#os.mkdir(dayzpath)


# In[284]:

if os.path.isdir(imgzdays) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(imgzdays)


# In[285]:

if os.path.isdir(rmgzdays) == True:
    print 'its true'
else:
    print 'its false'
    os.mkdir(rmgzdays)


# In[286]:

if os.path.isdir(metzdays)  == True:
    print 'its true'
else:
    print 'its failse'
    os.mkdir(metzdays)


# In[287]:

fullhom = ('/home/wcmckee/getsdrawndotcom/')


# In[288]:

os.listdir(fullhom + metzdays)


# In[289]:

#artlist


# In[290]:

httpad = ('http://getsdrawn.com/imgs')


# In[291]:

#im = Image.new("RGB", (512, 512), "white")
#im.save(file + ".thumbnail", "JPEG")


# In[292]:

rmgzdays = (dayzpath + '/reference')
imgzdays = (dayzpath + '/art')
metzdays = (dayzpath + '/meta')


# In[293]:

os.chdir(fullhom + metzdays)


# In[294]:

for lisr in lisrgc:
    gtdrndic.update({'title': lisr.title})
    lisauth.append(str(lisr.author))
    for osliz in os.listdir(fullhom + metzdays):
        with open(str(lisr.author) + '.meta', "w") as f:
            rstrin = lisr.title.encode('ascii', 'ignore').decode('ascii')
            f.write(rstrin)


# I have it creating a meta folder and creating/writing username.meta files. It wrote 'test' in each folder, but now it writes the photo author title of post.. the username/image data. 

# In[295]:

#os.listdir(dayzpath)


# Instead of creating these white images, why not download the art replies of the reference photo.

# In[296]:

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


# In[297]:

os.listdir('/home/wcmckee/getsdrawndotcom/imgs')


# In[298]:

#lisauth


# I want to save the list of usernames that submit images as png files in a dir. 
# Currently when I call the list of authors it returns Redditor(user_name='theusername'). I want to return 'theusername'.
# Once this is resolved I can add '-line.png' '-bw.png' '-colour.png' to each folder. 

# In[299]:

#lisr.author


# In[300]:

namlis = []


# In[301]:

#opsinz = open('/home/wcmckee/visignsys/index.meta', 'r')
#panz = opsinz.read()


# In[302]:

os.chdir('/home/wcmckee/getsdrawndotcom/' + rmgzdays)


# In[303]:

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


# In[304]:

apsize = []


# In[305]:

aptype = []


# In[306]:

basewidth = 600


# In[307]:

imgdict = dict()


# In[308]:

rmgzdays


# In[309]:

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


# In[310]:

imgdict


# In[311]:

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


# In[312]:

#basewidth = 300
#img = Image.open('somepic.jpg')
#wpercent = (basewidth/float(img.size[0]))
#hsize = int((float(img.size[1])*float(wpercent)))
#img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
#img.save('sompic.jpg')


# In[313]:

#os.chdir(metzdays)


# In[313]:




# In[314]:

#for numz in apsize:
#    print numz[0]
 #   if numz[0] > 800:
#        print ('greater than 800')
#    else:
#        print ('less than 800!')


# In[315]:

reliz = []


# In[316]:

for refls in os.listdir('/home/wcmckee/getsdrawndotcom/' + rmgzdays):
    #print rmgzdays + refls
    reliz.append(rmgzdays + '/' + refls)


# In[317]:

#reliz


# In[318]:

#aptype


# In[319]:

#opad = open('/home/wcmckee/ad.html', 'r')


# In[320]:

#opred = opad.read()


# In[321]:

#str2 = opred.replace("\n", "")


# In[322]:

#str2


# In[323]:

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


# In[324]:

docre = doc.render()


# In[325]:

#s = docre.decode('ascii', 'ignore')


# In[326]:

yourstring = docre.encode('ascii', 'ignore').decode('ascii')


# In[327]:

indfil = ('/home/wcmckee/getsdrawndotcom/index.html')


# In[328]:

mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()


# In[329]:

#os.system('scp -r /home/wcmckee/getsdrawndotcom/ wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom')


# In[330]:

#rsync -azP source destination


# In[331]:

#updatehtm = raw_input('Update index? Y/n')
#updateref = raw_input('Update reference? Y/n')

#if 'y' or '' in updatehtm:
#    os.system('scp -r /home/wcmckee/getsdrawndotcom/index.html wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/index.html')
#elif 'n' in updatehtm:
#    print 'not uploading'
#if 'y' or '' in updateref:
#    os.system('rsync -azP /home/wcmckee/getsdrawndotcom/ wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/')


# In[332]:

#os.system('scp -r /home/wcmckee/getsdrawndotcom/index.html wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/index.html')


# In[333]:

#os.system('scp -r /home/wcmckee/getsdrawndotcom/style.css wcmckee@getsdrawn.com:/home/wcmckee/getsdrawndotcom/style.css')


# In[334]:

#os.system("find /home/wcmckee/getsdrawndotcom/ -type f -name '*-reference.png'")


# In[335]:

lisfed = []


# In[336]:

#oswalk


# In[337]:

getdrndir = ('/home/wcmckee/getsdrawndotcom/')


# In[338]:

import walkdir 


# In[339]:

for oswalk in os.walk('/home/wcmckee/getsdrawndotcom/'):
    #if '*-reference.png' in oswalk:
    #print oswalk
    lisfed.append(oswalk)


# In[340]:

#for filz in walkdir.filtered_walk(getdrndir,  included_dirs='*-reference.png'):
 #   print filz


# In[341]:

walkz = ('/home/wcmckee/getsdrawndotcom/')


# In[342]:

walkz


# In[343]:

refim = []


# In[344]:

from walkdir import filtered_walk, dir_paths, all_paths, file_paths

files = file_paths(filtered_walk('/home/wcmckee/getsdrawndotcom/', depth=100, included_files=['*-reference.png']))


# In[368]:

for fil in files:
    #print fil
    refim.append(fil)


# In[373]:




# In[369]:

len(refim)


# In[404]:

nalis = []
imlis = []
cheklis = []


# In[405]:

for chet in refim:
    cheklis.append(chet[54:-14])
    imlis.append(chet[30:])


# In[414]:

filnalis = filter(None, cheklis)


# In[409]:

#def listurlz():
#    for ref in refim:
        #print ref[54:-14]
#        nalis.append(ref[54:-14])
        #imlis.append(ref[30:])
       # return nalis


# In[417]:

nelist = set(list(filnalis))


# In[421]:

len(nelist) 


# In[350]:

finel = []


# In[ ]:




# In[423]:

#filnalis


# In[351]:

for nel in nelist:
    #print nel()
    finel.append(nel)
    finel.sort
    


# In[352]:

finel.sort


# In[353]:

feralis = []


# In[354]:

for fil in finel:
    #print fil
    feralis.append(fil)


# In[355]:

apzlis = []


# In[356]:

for ferz in feralis:
    #print ferz
    for fea in ferz:
        #print fea
        apzlis.append(fea)


# In[357]:

#sorted(feralis)


# In[358]:

import random


# In[359]:

randz = random.randint(0, len(nelist))


# In[360]:

randz


# In[429]:

newzlist = list(nelist)


# In[431]:

ranred = r.get_redditor(newzlist[randz])


# In[432]:

print ranred.get_submitted


# In[487]:

comza = ranred.get_submitted()


# In[487]:




# In[488]:

for rcom in comza:
    print rcom.subreddit
    #if 'redditgetsdrawn' in rcom.subreddit:
    #    print rcom
    print rcom.created


# In[447]:

deepmz = ranred.name


# In[448]:

for deep in deepmz:
    print deep


# In[434]:

rsubm = ranred.get_submitted


# In[435]:

for rsm in rsubm():
    print rsm


# In[436]:

ozalis = []


# In[ ]:

for fera in feralis:
    print len(fera)
    randz = random.randint(0, len(fera))
    for fea in fera:
        #print fea
        ozalis.append(fea)
        


# In[ ]:

#randz


# In[ ]:

#listurlz()


# In[ ]:

for ref in refim:
    #print ref[54:-14]
    nalis.append(ref[54:-14])
    imlis.append(ref[30:])
#54


# In[ ]:

imlis[0]


# In[ ]:

nalis.sort()


# In[ ]:

len(nalis)


# In[ ]:




# In[ ]:

filnalis = filter(None, nalis)


# Working good at extracting usernames from folders. Need to look up usernames on reddit. 

# In[ ]:

#for filna in filnalis:
#    usrz = r.get_redditor(filna)


# In[ ]:

#itfil = iter(filnalis)


# In[ ]:

#filter(itfil)


# In[ ]:

#for itz in itfil:
#    print itz


# In[ ]:

for filn in filnalis:
    print filn


# In[ ]:

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
        for refz in imlis:
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


# In[ ]:

doctea = docall.render()


# In[ ]:

strng = doctea.encode('ascii', 'ignore').decode('ascii')


# In[ ]:

getdall = ('/home/wcmckee/getsdrawnall/index.html')


# In[ ]:

msav = open(getdall, 'w')
msav.write(strng)
msav.close()

