#!/usr/bin/env python
# coding: utf-8

# # Pattern assignment

# In[3]:


n=(int(input("Enter the number of rows")))
for i in range (n):
    for j in range (i+1):
        print(j+1,end=" ")
    print()


# In[11]:


n=(int(input("Enter the number of rows")))
for i in range (n):
    for j in range (i,-1,-1):
        print(j+1,end='')
    print()


# In[18]:


n=(int(input("Enter the number of rows")))
for i in range (1,n+1):
    for j in range (1,i+1):
        print(i,end='')
    print()


# In[20]:


n=(int(input("Enter the number of rows")))
for i in range (1,n+1):
    for j in range (1,i+1):
        print(i,end='')
    print()


# In[29]:


n=(int(input("enter no. of rows")))
for i in range (n):
    for j in range (i+1):
        print(n-i,end='')
    print()


# In[30]:


n=(int(input("enter no. of rows")))
for i in range (n):
    for j in range (i+1):
        print(n-j,end='')
    print()


# In[3]:


n=(int(input("enter no. of rows")))
for i in range (n):
    for j in range (i,-1,-1):
        print(n-i,end='')
    print()


# In[34]:


n=(int(input("enter no. of rows")))
for i in range (n):
    for j in range (i+1):
        print(j+1,end='')
    print()


# In[43]:


n=(int(input("enter no. of rows")))
for i in range (n):
    for j in range (n-i-1):
        print(" ",end=" ")
    for j in range (i,-1,-1):
        print(n-j,end='')
    print()


# In[64]:


n=(int(input("enter no. of rows")))
for i in range (n):
    for j in range (n-i-1):
        print(" ",end=" ")
    for j in range (i+1):
        print(j+1,end=" ")
    print()


# ## Pattern1

# In[65]:


n=(int(input("enter the no. of rows")))
for i in range(n):
    for j in range (i+1):
        print(j+1,end=" ")
    print()


# ## Pattern2

# In[69]:


n=(int(input("entr no. of rows")))
for i in range (na):
    for j in range (i+1):
        print(i+1,end=" ")
    print()


# ## Pattern3

# In[75]:


n=(int(input("entr no. of rows")))
for i in range (n):
    for j in range (i+1):
        print(j+1,end=" ")
    print()
for i in range (n-2,-1,-1):
    for j in range (i,-1,-1):
        print(j+1,end=" ")
    print()


# ## pattern4

# In[86]:


n=(int(input("Enter no. of rows")))
for i in range (n,-1,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()
for i in range (n):
    for j in range (i+1):
        print(j+1,end=" ")
    print()
    


# ## pattern5

# In[99]:


n=(int(input("Enter no. of rows")))
for i in range (n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
for i in range (n):
    for i in range(i,-1,-1):
        print(i+1,end=" ")
    print()


# In[104]:


n=(int(input("Enter no. of rows")))
for i in range (n):
    for j in range(i+1,0,-1):
        print(i+1,end=" ")
    print()


# In[105]:


n=(int(input("enter no. of rows")))
for i in range (n):
    for i in range(i,-1,-1):
        print(i+1,end=" ")
    print()


# In[114]:


n=(int(input("enter no. of rows")))
for i in range (n):
    for j in range(i+1):
        print(n-j,end=" ")
    print()


# In[118]:


n=(int(input("enter no. of rows")))
for i in range (n,0,-1):
    for j in range(i):
        print(n-j,end=" ")
    print()


# In[121]:


n=(int(input("enter no. of rows")))
for i in range (n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()


# In[124]:


n=(int(input("enter no. of rows")))
for i in range (n,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()


# ## Pattern10

# In[23]:


n=(int(input("enter no. of rows")))
a=1
for i in range (1,n+1):
    for j in range(1,i+1):
        print(a,end="              ")
        a+=1
    print()


# ## pattern11

# In[29]:


n=(int(input("enter no. of rows")))
for i in range (n):
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()


# In[38]:


n=(int(input("enter no. of rows")))
a=1
for i in range (1,n):
    for j in range(1,i+1):
        print(a,end=" ")
        a+=1
    print()


# In[16]:


n=(int(input("enter no. of rows")))
for i in range (n):
    a=i+1
    b=n-1
    for j in range(i+1):
        print(format(a),end=" ")
        a=a+b
        b=b-1
    print()


# ## Pattern 12

# In[17]:


n=(int(input("enter no. of rows")))
for i in range (n):
    a=i+1
   # b=n-1
    for j in range(i+1):
        print(format(a),end=" ")
        a=a+5
       # b=b-1
    print()


# In[6]:


n=(int(input("enter no. of rows")))
for i in range (n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
for i in range (n-1):
    for j in range (n-i-1):
        print(" ",end=" ")
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()


# ## PATTERN 13

# In[16]:


def solve(n):
    for i in range(n+1):
        for j in range(n-i):
            print(' ', end='')
            C = 1
    for j in range(1, i+1):
        print(C, ' ', sep='', end='')
        C = C * (i - j) // j
        print()
n = 5
solve(n)


# In[22]:


# Print Pascal's Triangle in Python

# input n
n = 6

for i in range(1, n+1):
	for j in range(0, n-i+1):
		print(' ', end='')

	# first element is always 1
	C = 1
	for j in range(1, i+1):

		# first value in a line is always 1
		print(' ', C, sep='', end='')

		# using Binomial Coefficient
		C = C * (i - j) // j
	print()


# ## pattern13

# In[3]:


import math as m
m.factorial(5)


# In[25]:


import math
n=int(input("enter n"))
for i in range (n):
    print(" "*(n-i),end=" ")
    for j in range (i+1):
        a=int((m.factorial(i)/((m.factorial(i-j))*(m.factorial(j)))))
        print(a,end="  ")
    print()


# ## pattern14

# In[46]:


n=(int(input("enter no. of rows")))
for i in range (1,n+1):
    print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range (i-1,0,-1):
        print(j,end=" ")
    print()
#for i in range (n-1):
   # for j in range (n-i-1):
       # print(" ",end=" ")
  #  for j in range(i+1,0,-1):
       # print(j,end=" ")
   # print()


# ## Pattern15

# In[55]:


n=(int(input("enter no. of rows")))
for i in range (n,-1,-1):
    print(" "*(n-i),end=" ")
    for j in range(i+1):
        print(j+1,end=" ")
    print()


# ## pattern 16

# In[ ]:


n=(int(input("enter no. of rows")))
for i in range (n):
    print(" "*(n-i),end=" ")
    for j in range(i+1):
        print(j+1,end=" ")
    print()
for i in range (n,0,-1):
    print(" "*(n-i+2),end=" ")
    for j in range (i-1):
        print(j+1,end=" ")
    print()


# # STAR PATTERN

# In[2]:


n=int(input("Enter no. of rows"))
for i in range (n):
    for j in range (i+1):
        print("*",end=" ")
    print()


# In[8]:


n=int(input("Enter n: "))
a=1
for i in range (n):
    for j in range(i+1):
        print(i+1,end=" ")
        a+=1
    print()


# In[ ]:




