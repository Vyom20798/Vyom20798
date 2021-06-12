#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Fibonacci series
Number = int(input("How many Number? "))

# in fibonacci 1st term is 0 and 2nd term is 1 hence: 
n1, n2 = 0, 1
count = 0

if Number == 1:
    print("Fibonacci sequence upto",Number,":")
    print(n1)
else:
    print("Fibonacci sequence: ",  end=" ")
    while count < Number:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1


# In[13]:


#Geometric_progression
def GP(a,r,n):
    for i in range (0,n):
        formula = a*pow(r,i)
        print ( formula, end =" ")


# In[33]:


GP(2,8,10)


# In[ ]:




