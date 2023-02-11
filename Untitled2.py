#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("For Loop Example:")
for i in range(1, 11):
    print(i)

    
print("\nWhile Loop Example:")
j = 1
while j <= 10:
    print(j)
    j += 1


# In[18]:


import random
my_list = ["unnamed_1","Ruslan","guest123","Ghost","Lich"]
my_list2= ["Bronze", "Silver", "Gold", "Diamond"]
for index in range(len(my_list)):
  print(f"{my_list[index]} won {random.randint(1,9)} {my_list2[random.randrange(0,4)]}")


# In[34]:


a = 9
b = 5
if(a<b):
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)


# In[45]:


a = 9
b = 2

a = a - (1 - a % 2)

for i in range(a, b-1, -2):
    print(i)


# In[56]:


N = 9
lost = 1
summ=0
for i in range(1,N+1):
    summ+=i
for i in range(N-1):
    if(i+1!=lost):
        summ-=i+1
    else:
        summ-=N
        
print(summ)


# In[ ]:




