#!/usr/bin/env python
# coding: utf-8

# In[17]:


#To check if number is odd or even
def Odd_or_even(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"


# In[24]:


Odd_or_even(43.4)


# In[25]:


#Alternatively


# In[43]:


num = int(input("Enter Any Number: "))
if num%2==0:
    print("Even")
elif num%2!=0:
    print("Odd")

