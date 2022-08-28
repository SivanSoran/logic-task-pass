#!/usr/bin/env python
# coding: utf-8

# In[ ]:


min = int(input("Starting Range: "))
max = int(input("Ending Range: "))

for a in range(min,max + 1):
   if a > 1:
       for i in range(2,a):
           if (a % i) == 0:
               break
       else:
           print(a)


# In[ ]:





# In[ ]:




