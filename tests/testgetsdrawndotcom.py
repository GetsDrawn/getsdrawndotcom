
# coding: utf-8

# These are test cases. 
# 
# Things I need to test.
# Opening up json data from reddit. 
# converting json data to dict.
# 

# In[52]:

import unittest
from mock import Mock
import os
import socket
import getpass

#from getsdrawndotcom import pathcheck

import getsdrawndotcom

#from getsdrawndotcom import 


# In[45]:

getsdrawndotcom.


# In[46]:

jsexam = open('/home/wcmckee/signinlca/signups.json', 'r')


# In[47]:

mfunc = Mock.return_value = jsexam.read()


# In[48]:

mfunc


# In[49]:

class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):  ## test method names begin 'test*'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)
        


# In[50]:

class TestPath(unittest.TestCase):
    def set_up(self):
        #Setup creates the json file that is tested. 
        self.
    def test_dirc_exist(self):
        #This test is checking the path exists.
        self.('/home/wcmckee')
        self.assertRaises('TypeError')
    
    
    #def test_open_meta(self):
        #This test checks it can open/read the meta file
        #with open(getsdrawndotcom., 'r') as indexfil:
            #assert indexfil.read()
'''            
    def test_create_dict(self):
        #This tests creating dict
        
    def test_update_dict(self):
        #This tests updating dict update with key title and value is the dict file title.
        
    def test_conv_json(self):
        #THis tests converting the dict to a json file. 
        
    def test_save_json(self):
        #This tests saving the json file.
        
    def test_trans_json(self):
        #This tests transfer of json file
        
    def test_read_json(self):
        #This tests reading the json file. 
        
    def test_logo_dirc(self):
        #This tests for is there a logo in the directory. 
    
    def test_write_logo(self):
        #This tests creating index.html with logo.png
        
    
        
        #for lisr in lisrgc:
        #    gtdrndic.update({'title': lisr.title})
        #    lisauth.append(str(lisr.author))
        #    for osliz in os.listdir(fullhom + metzdays):
        #        with open(str(lisr.author) + '.meta', "w") as f:
        #            rstrin = lisr.title.encode('ascii', 'ignore').decode('ascii')
        #            f.write(rstrin)
        
'''


# In[ ]:

if __name__ == '__main__':
    unittest.main()

