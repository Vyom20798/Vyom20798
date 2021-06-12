#!/usr/bin/env python
# coding: utf-8

# In[15]:


# .append() is use to new element in the list

Vehicles = ["Car", "Bus", "Train", "Boat"]    
print("Vehicle List :", Vehicles)   
Add_Vehicle = input("Please enter a name: \n")  
Vehicles.append(Add_Vehicle)    
print('Updated Vehicle List :', Vehicles)  


# In[21]:


#To be more precise, we can provide index using .insert(index,value)

list1 = [10, 20, 30, 40, 50]  
print("Original List: ", list1)    
list2 = list1.insert(3, 77)  
print("Updated list ",list1)    
n = int(input("Enter number \n"))    
index = int(input("Enter index \n"))    
list1.insert(index, n)  
print('Updated Numbers List:', list1)  


# In[32]:


#Using extend

Numbers = [1,2.3,45,678, 874.9]
Numbers.extend(["678"])
print(Numbers)
Numbers.extend((40, 30))
print(Numbers)  
Numbers.extend("Banana")  
print(Numbers)  


# In[37]:


#to delete we use 
#remove() removes that element
#pop() removes the index 
#clear() empty list
#del() del do all the function of the above 3

Company= ["Amazon", "Flipkart", "Ebay", "BigBasket"]
print(Company)
Company.remove("BigBasket")
print(Company, "\n Used .remove")
Company.pop(-2)
print(Company, "\n used .pop")


# In[38]:


#list comprehensions 

eleven=[11,22,33,44,55,66]
print([i for i in list1 if i % 2 == 0])


# In[40]:


eleven=[11,22,33,44,55,66]
print([i for i in eleven if i % 2 != 0])


# In[41]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[49]:


#converting List to set, we use set()

Fruits = ["Apple", "Mango", "Banana", "Orange", "Guava", "Pineapple", "Strawberry", "Grapes"]  
Coversion=set(Fruits)
print(Coversion)  


# In[16]:


#some most used list features

Fruits = ["Apple", "Mango", "Banana", "Orange", "Guava", "Pineapple", "Strawberry", "Grapes"]  
print (Fruits[1])
print (Fruits[2:5])
print (Fruits[-8:-3])
print (Fruits[:2])
print (Fruits[3:])
Fruits.sort()
print (Fruits)
Fruits.sort(reverse=True)
print (Fruits)


# In[ ]:




