#!/usr/bin/env python
# coding: utf-8

# In[6]:


def lcm(x, y):  
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm  
  
  
value1 = int(input("Enter first number: "))  
value2 = int(input("Enter second number: "))  
print("The L.C.M. of", value1,"and", value2,"is", lcm(value1, value2))  


# In[ ]:




