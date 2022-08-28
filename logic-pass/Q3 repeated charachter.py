#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import collections


# In[ ]:


string = str (input ("Type String:"))
frequencies = collections.Counter(string)
key = str(input("Repeated Char:"))
print (frequencies[key])


# In[ ]:




