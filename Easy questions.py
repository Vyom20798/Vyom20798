#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Miles to kilometer
# 1mile = 1.6km

mls=float(input("Enter miles"))
km= 1.6*mls
print(mls ,"miles is" ,km,"km" )


# In[15]:


# checking leap year
# Number should be completely divided by 4, centuries should be completely divided by 4

year = int(input("Enter a year: "))  
if year % 4 == 0:  
    if year % 100 == 0:  
        if (year % 400) == 0:  
            print(year,"is a leap year")  
        else:  
            print(year,"is not a leap year")  
    else:  
        print(year,"is a leap year")  
else:  
    print(year,"is not a leap year")  


# In[19]:


#Prime Number. Number should have only 1 factor

number = int(input("Enter a numberber: "))  
  
if number > 1:  
    for x in range(2,number):  
        if (number % x) == 0:  
            print(number,"is not a prime numberber")    
            break  
    else:  
        print(number,"is a prime numberber")  
else:  
    print(number,"is not a prime numberber")  

