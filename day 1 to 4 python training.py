#!/usr/bin/env python
# coding: utf-8

# In[ ]:


day 1


# In[1]:


print('hello world')


# In[ ]:





# In[2]:


print('hello all welcome to the python world')


# In[ ]:





# In[ ]:


day 2


# In[ ]:


#1. understanding the variables in python.


# In[ ]:





# In[10]:


x = 5 # x is holding some value

y= 4 # y is holding some value


# In[11]:


x+y


# In[ ]:





# In[12]:


#rules for the declaring the variable names

#commenting the line in python 

#something


# In[13]:


#1. rule ----> there should be no gap in variable names.


# In[14]:


find name = 'shaik'


# In[17]:


first_name = 'shaik'

firstname ='shaik'

#both are valid


# In[ ]:


#2. it should not start with numbers

1xyz = 1000 -------> invalid declaration

xyz1 = 1000 -------> valid declaration


# In[ ]:


#3. it should not start with any special charactors.

@abc = 100 --------> invalid dec

abc$ = 100 --------> valid dec


# In[ ]:





# In[ ]:


#introduction to data types in python.


1.String -------> str
2.List -------> list
3.Tuple -------> tuple
4.Dictionary -----> dict


# In[ ]:


#python is a sensitive language



# In[ ]:


introducing to string !!


# In[ ]:


def: A string is nothing but series of characters.
    
features:
    
A string is an immutable data type (which cannot be changed / modfied once its gets assigned)

how to create / define string.

3 possible ways by which we can able to create string.

1. ' '------> single quotes
2. "" -------> double quotes
3. """ """------> triple quotes


# In[23]:


name = 'vikram'


# In[24]:


print(name)


# In[25]:


type(name)


# In[26]:


name2 = "odedara"


# In[27]:


print (name2)


# In[28]:


name3 = """keshav"""


# In[29]:


print(name3)


# In[30]:


type(name3)


# In[31]:


#introduction to string methods.


# In[ ]:


#enhanacement of the code.


# In[32]:


name2 = "odedara"

print(name2) #not the right format.


# In[33]:


print(name2.title()) #title case ---->


# In[34]:


print(name3.upper()) # upper case.


# In[35]:


print(name3.lower()) # lower case


# In[36]:


#using the concpt of f string!!


f_name = 'kumar'
l_name = 'ravi'

full_name =f" {f_name} {l_name}" # f "place holders"

print(full_name)


# In[ ]:





# In[37]:


#enhancement of the code.


f_name = 'vikram'
l_name = 'odedara'

full_name = f"Excellent work, keep up the same {f_name} {l_name}"

print(full_name)


# In[ ]:





# In[ ]:


day 3


# In[ ]:





# In[38]:


#continuation with Strings:


# In[39]:


#adding whitespaces to strings:


# In[40]:


print('python')

print('\tpython') #\t-----> tab delimeter ---->


# In[41]:


print("languages:\npython\njava\nswift\nruby") 


# In[42]:


#removing whitespaces!

fav_lang = "python"  #rightside

fav_lang2 = "java" #leftside

print(fav_lang)
print(fav_lang2)


# In[43]:


fav_lang.rstrip()


# In[44]:


fav_lang2.lstrip()


# In[46]:


fav_lang3 = "html"

print(fav_lang3)


# In[47]:


fav_lang3.strip()


# In[ ]:


#numbers ---->


# In[48]:


2+3 #integers -----> int


# In[ ]:


int


# In[50]:


2-3


# 

# In[51]:


2*3


# 

# In[52]:


2**2


# In[53]:


2**3


# In[54]:


2**5


# In[ ]:


float --->


# In[57]:


3.0+5.1


# In[58]:


x= 1.2

y= 3.2


# In[ ]:





# In[59]:


z=x+y

print(z)


# In[60]:


type(z)


# In[ ]:


#introdusing to list data type:


# In[ ]:


list is a call of a particuler order.

how to define a list -----> [] ------> square brackets

what kind of data type is a list is ---> mutable data type!!

we can able to change/modify once we assign the elements/items to it.


# In[ ]:





# In[61]:


students = ['hema','vivek','devi','akbar','ashok','geetha']

print(students)


# In[62]:


type(students)


# In[ ]:


#introduction to indexing:

indexing will be starting from 0.....!!


# In[ ]:





# In[63]:


#how to access the elements in a list:


print(students[2])


# In[64]:


print(students[5])


# In[67]:


#enhancement of the code....

print(students[5].title())


# In[68]:


#further enhanacement !!

message = f"you are doing a good job,{students[4].title()}"

print(message)


# In[ ]:





# In[ ]:


day 4


# In[ ]:





# In[ ]:


#

#adding changing and removing elements from the list!!!!!


# In[69]:


my_students = ['divya','srinivas','ranga','akbar','vinod']

print(my_students)


# In[ ]:


how to remvoe the elements !!


# In[70]:


my_students.append('geetha')  #.append --- makes the element to be added at the end of the list.

print(my_students)


# In[ ]:


req: to add a new students in the inbox ----> Harsha.


# In[72]:


my_students[1] = 'harsha' #modifying ---- the new elemet.

print(my_students) # 6 elements --->


# In[ ]:


#insertng the in to a list. 3 index ----> sireesha


# In[74]:


my_students.insert(3,'sireesha')


print(my_students)  #7 elements 


# In[ ]:


# how to remove elements from the list ---->


# In[76]:


del my_students[0]

print(my_students)


# In[ ]:





# In[ ]:


removing the elements by using the pop() menthod.

#it will be maintaining carboncopy ofthe deleted items.

#the dafault nature, it will be deleting the elements from the end.


# In[ ]:





# In[77]:


my_students.pop()


# In[78]:


print(my_students)


# In[79]:


my_students.pop(1)


# In[80]:


print(my_students)


# In[ ]:





# In[ ]:


organising a list.


# In[83]:


students = ['suresh','swamy','sandhya','vivek','zakir']

print(students)


# In[ ]:


req: org the group of the students in an alphabetical order.


# In[85]:


students.sort() #a-z, 

print(students) #sort ---> it will make permanent change


# In[ ]:





# In[86]:


print(students)


# In[ ]:





# In[ ]:


req: temp sorting we need it has to go back to original position:


# In[ ]:





# In[88]:


students2 = ['poojitha','aditya','sahil','vidya','hema']

print(students2)


# In[89]:


print('here is the sorted list:')
print(sorted(students2)) #sorted ---- which we will be using for temp sorting


# In[ ]:





# In[90]:


print(students2)


# In[ ]:





# In[ ]:


sort vs sorted


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




