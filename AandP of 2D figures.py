#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Square, Rectangle, Triangle, Circle, Rhombus, Paraellogram

shape=input("Enter figure: ")
if shape=="square":
    a1=int(input("Enter side: "))
    A=a1*a1
    P=4*a1
    print("Area of square is", A,"sq unit")
    print("Perimeter of square is",P,"unit")   
elif shape=="rectangle":
    a1=int(input("Enter length"))
    b1=int(input("Enter breadth"))
    A=a1*b1
    P=2*(a1+b1)
    print("Area of rectangle is", A,"sq unit")
    print("Perimeter of rectangle is",P,"unit")    
elif shape=="circle":
    a1=int(input("Enter Radius"))
    A=3.14*(a1**2)
    P=2*3.14*a1
    print("Area of Cirlce is", A,"sq unit")
    print("Perimeter of Circle is",P,"unit")    
elif shape=="rhombus":
    a1=int(input("Enter diagonal 1"))
    b1=int(input("Enter diagonal 2"))
    c1=int(input("Enter side "))
    A=(a1*b1)/2
    P=4*(c1)
    print("Area of rhombus is", A,"sq unit")
    print("Perimeter of rhombus is",P,"unit")    
elif shape=="parallelogram":
    a1=int(input("Enter base"))
    b1=int(input("Enter height"))
    c1=int(input("Enter side "))
    d1=int(input("Enter side 2"))
    A=a1*b1
    P=2*(c1+d1)
    print("Area of Parallelogram is", A,"sq unit")
    print("Perimeter of Parallelogram is",P,"unit")    
elif shape=="triangle":
    formula=int(input("Choose either 1 or 2: "))
    if formula== 1:
        a=int(input("Enter 1st side: "))
        b=int(input("Enter 2nd side: "))
        c=int(input("Enter 3rd side: "))
        if a+b>c:
            print ("It is a triangle")    
        else:
            print ("Not a triangle") # I need your advice how to stop loop to move forward if a+b!=c
        a1=int(input("Enter base: "))
        b1=int(input("Enter height: "))
        A=a1*b1
        P=a+b+c
        print("Area of Triangle is", A,"sq unit")
        print("Perimeter of Triangle is",P,"unit")
    elif formula == 2:
        a1=int(input("Enter side: "))
        b1=int(input("Enter side 2: "))
        c1=int(input("Enter side 3: "))
        s=(a1+b1+c1)/2
        print("s =", s)
        s1=s*(s-a1)*(s-b1)*(s-c1)
        A=s1**0.5
        P=a1+b1+c1
        print("Area of Triangle is", A,"sq unit")
        print("Perimeter of Triangle is",P,"unit")


# In[ ]:




