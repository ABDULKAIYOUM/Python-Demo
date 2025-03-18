#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Statements(if, elif,else)

loc = 'Street'

if loc == 'Auto Shop':
    print('Buy Audi')
elif loc == 'Bank':
    print('Money')
else:
    print('No Idea')


# In[2]:


# For loops

mylist = [1,2,3,4,5]

for num in mylist:
    print("Have a good day")


# In[3]:


for num in mylist:
    if num % 2 == 0:
        print('Even Number')
    else:
        print(f'{num} is Odd Number')


# In[4]:


total_sum = 0

for num in mylist:
    total_sum = total_sum + num

print(total_sum)


# In[5]:


total_sum = 0

for num in mylist:
    total_sum = total_sum + num

    print(total_sum)


# In[6]:


mystring = 'Hello World!'

for letters in mystring:
    print(letters)


# In[7]:


# Alternative

for letters in 'Europe':
    print(letters)


# In[ ]:




