
# coding: utf-8

# In[ ]:

import os


# In[28]:

class getsdrawn(object):
    def __init__(self):
        #gdimgs is a dict object of rgd data.
        self.gdimgs = dict()
    
    def dictaddconts(self, username):
        self.gdimgs.update({'username': username})
    

    def pathcheck(self, pathdirc):
        if os.path.isdir(pathdirc) == True:
            assert 'its true'
        else:
            assert 'its false'
            os.mkdir(pathdirc)

    def openmetafil(metaname):
        with open(metaname, 'r') as indexfil:
            return indexfil.read()
        #panz = opsinz.read()
    
    #def create


# In[26]:




# In[26]:




# In[ ]:



