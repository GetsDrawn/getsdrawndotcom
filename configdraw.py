
# coding: utf-8

# <h1>Config Draw</h1>
# 
# <h3>Configuration file Getsdrawn</h3>
# 
# Script to create and edit the getsdrawndotcom config file.
# 
# Things this config file does:
# 
# Change the folder where the files saved.
# 
# Change folder date system (/home/wcmckee/blah/2015/02/20/username.png) or file date system (/home/wcmckee/blah/username-2015-02-20.png)
# 
# Specify which subreddit (or multi) to download from
# 
# ANYMORE CONFIGS NEEDED?
# 
# Config max/min size of files downloaded?
# 
# Config how often to run the script. 
# 
# Configfig where logo is, use multi logos (switch hour etc)
# 
# Config css. Background color etc.
# 
# Need to write another script that will open up this config file and use it to run gotdrawn script. 

# In[26]:

import os
import configparser


# In[27]:

config = configparser.RawConfigParser()


# In[28]:

config.read('/home/wcmckee/gotdrawn/config.cfg')


# In[29]:

config.add_section('subredinfo')


# In[30]:

whatsub = raw_input('What subreddit: ')


# In[31]:

inputfol = raw_input('Dir where to save: ')


# In[32]:

outfilda = raw_input('Output folder date y/n: ')

outfilez = raw_input('Output file date y/n: ')


# In[33]:

outfilq = ''
outfilez = ''


# In[34]:

if 'y' in outfilda:
    outfilq = True
else:
    print ('Not outputing folder')
    outfilq = False
    
if 'y' in outfilez:
    outfilez = True
else:
    outfilez = False


# In[36]:




# In[37]:

config.set('subredinfo', 'subbreddit', whatsub)
config.set('subredinfo', 'dirpath', inputfol)
config.set('subredinfo', 'outputfolder', outfilq)
config.set('subredinfo', 'outputfile', outfilez)


# In[38]:

with open('/home/wcmckee/gotdrawn/config.cfg', 'wb') as configfile:
    config.write(configfile)


# In[ ]:



