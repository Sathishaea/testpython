#!/usr/bin/env python
# coding: utf-8

# # Write a program to find out the prime numbers 

# In[38]:


test=int(input("Enter upper limit: "))
for a in range(2,test+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)


# # Q2: write a program to create the equation (a+b+c) *  (a-b-c) * ab + a^2 + b ^2 + (abc)^3

# In[40]:


import numpy as np 
def Guvipython(a,b,c):
    add = a+b+c 
    sub = a-b-c
    mul =a*b
    power1= a**2
    power2= b**2
    abc=  a*b*c
    cube= abc**3
    total = add*sub*mul+power1+power2+cube
    return total
calculated = Guvipython(1,2,3)
print (calculated)


# # Q3) urlist = ['wood','knife','axe'] , mylist = ['tree', 'apple', 'mango', 'melon'] – combine two lists
# 

# In[41]:


urlist = ['wood','knife','axe'] 
mylist = ['tree', 'apple', 'mango', 'melon'] 
finallist = urlist+mylist
print (finallist)


# In[44]:


urlist = ['wood','knife','axe'] 
mylist = ['tree', 'apple', 'mango', 'melon'] 
urlist.extend(mylist)
print (urlist)


# # write a program for natural number based on user input

# In[45]:


number = int(input("Please Enter any Number: "))

print("The List of Natural Numbers from 1 to {0} are".format(number)) 

for i in range(1, number + 1):
    print (i, end = '  ')


# In[13]:


def checknatnum(n):
    if int(n)>0:
        return True
    else:
        return False
checknatnum(0)


# # write class and function for the equation sqrt(x1-x2) ^ 2 + sqrt( y1 – y2 ) ^2 using try except handling

# In[28]:


import math
class Calulation:
    def __init__(self, X1, X2,Y1,Y2):
        self.X1=X1
        self.X2=X2
        self.Y1=Y1
        self.Y2=Y2
        try:
            c1=math.sqrt(X1 - X2)**2
            c2=math.sqrt(Y1 - Y2)**2
            c3 =c1+c2
            print(c3)
        except:
             print("Check ur input- X1 should be greater than X2 and also Y1 Should be greater than Y2")
s=Calulation(1,2,4,5)


# In[46]:


import math
class Calulation:
    def __init__(self, X1, X2,Y1,Y2):
        self.X1=X1
        self.X2=X2
        self.Y1=Y1
        self.Y2=Y2
        try:
            c1=math.sqrt(X1 - X2)**2
            c2=math.sqrt(Y1 - Y2)**2
            c3 =c1+c2
            print(c3)
        except:
             print("Check ur input- X1 should be greater than X2 and also Y1 Should be greater than Y2")
s=Calulation(2,1,4,3)


# # Name  = “Guvi python”  - write a program to get “python” word from the string

# In[24]:


string = "Guvi python"
words = string.split(' ')[1]
print(words)


# In[ ]:





# # Using class and function - Write a program for palindrome Ex. Madam

# In[31]:


def isPalindrome(s):
    return s == s[::-1]
s = "madam"	
ans = isPalindrome(s)
 
if ans:
    print("Yes, its a palindrome")
else:
    print("Not a Palindrome")


# In[32]:


def isPalindrome(s):
    return s == s[::-1]
s = "test"	
ans = isPalindrome(s)
 
if ans:
    print("Yes, its a palindrome")
else:
    print("Not a Palindrome")


# # using file handling – write a text file in ur system with “hello world”

# In[34]:


from pathlib import Path

dir_path = Path('C:\Pyth')
file_name = "test.txt"
file_path = dir_path.joinpath(file_name)

# check that directory exists
if dir_path.is_dir():
    with open(file_path, "w") as f:
        f.write("hello world")
        print('File was created.')
else:
    print("Directory doesn\'t exist.")


# # create option button using tkinter GUI in python

# In[36]:


import tkinter as tk
root = tk.Tk()
v = tk.IntVar()
tk.Label(root, 
        text="""Choose a 
programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()

tk.Radiobutton(root, 
               text="Python",
               padx = 50, 
               variable=v, 
               value=1).pack(anchor=tk.W)

tk.Radiobutton(root, 
               text="Perl",
               padx = 50, 
               variable=v, 
               value=2).pack(anchor=tk.W)
tk.Radiobutton(root, 
               text="Java",
               padx = 50, 
               variable=v, 
               value=2).pack(anchor=tk.W)
root.mainloop()


# # Q10) .Keep only numbers from the following string x = “ 89e9jcd^o38829@3%3,/mkl$w1”

# In[37]:


inp_str = "89e9jcd^o38829@3%3,/mkl$w1"
num = ""
for c in inp_str:
    if c.isdigit():
        num = num + c
print("Extracted numbers from the list : " + num) 


# In[ ]:




