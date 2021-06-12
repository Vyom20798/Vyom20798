#!/usr/bin/env python
# coding: utf-8

# In[3]:


hrs = float(input("Enter hours: "))
h= float(hrs) 
rate = float(5.5)

if h <= 40:
    pay = h*rate
elif h > 40:
    pay = ((rate*40)+(h-40)*rate*2)  

print ("Your pay is Rs.%d"%pay)

