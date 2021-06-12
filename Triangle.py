#!/usr/bin/env python
# coding: utf-8

# In[3]:


#To check if the gven figure is triangle

a=int(input("Enter 1st side: "))
b=int(input("Enter 2nd side: "))
c=int(input("Enter 3rd side: "))

if a+b>c:
    print ("It is a triangle")
else:
    print ("Not a triangle")


# In[ ]:


#Pythagorous Theorem

a=int(input("Enter side: "))
b=int(input("Enter side: "))

c1=(a**2)+(b**2)
c=c1**0.5
print("The third side of triangle is",round(c,2),"unit")

