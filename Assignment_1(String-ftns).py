#!/usr/bin/env python
# coding: utf-8

# In[1]:


str = "PARVEEN bibi"
print (str.capitalize())


# In[2]:


str = "PARVEEN bibi"
print (str.casefold())


# In[3]:


str = "PARVEEN bibi"
rslt = str.center(25)
print (rslt)


# In[4]:


str = "PARVEEN bibi"
rslt = str.count('A')
print (rslt)

str1 = [1,3,5,3,2]
rslt = str1.count(str1[0])
print(rslt)


# In[5]:


str = "PåRVEEN bii"
rslt = str.encode()
print (rslt)


# In[6]:


str = "PARVEEN bibi"
rslt = str.endswith(',')
print (rslt)

str = "PARVEEN bibi."
rslt = str.endswith('.')
print (rslt)


# In[7]:


str = "PA\tRVEEN\tbibi"
rslt = str.expandtabs()
print (rslt)
rslt = str.expandtabs(3)
print (rslt)


# In[8]:


str = "PARVEEN bibi"
rslt = str.find("i")
print (rslt)


# In[9]:


name = "Parveen"
f_name = "Faisal Malook"
uni = "Bahria"
score = 100

txt = """
Name:{0}
Father Name:{1}
University:{2}
Score:{3}
"""

print(txt.format(name,f_name,uni,score))


# In[10]:


point = {'x':2, "y":0}
print('{x} {y}'.format_map(point))
point = {'x':2, "y":0}
print('{y} {x}'.format_map(point))


# In[11]:


str = "PARVEEN bibi"
rslt = str.index("E")
print (rslt)


# In[12]:


str = "PARVEEN bibi"
rslt = str.isalnum()
print (rslt)

str = "3"
rslt = str.isalnum()
print (rslt)

str = "abc3"
rslt = str.isalnum()
print (rslt)


# In[13]:


str = "PARVEEN bibi"
rslt = str.isalpha()
print (rslt)

str = "3"
rslt = str.isalpha()
print (rslt)

str = "abc"
rslt = str.isalpha()
print (rslt)


# In[14]:


str = "PARVEEN bibi"
rslt = str.isascii()
print (rslt)

str = "3"
rslt = str.isascii()
print (rslt)

str = "Ståle"
rslt = str.isascii()
print (rslt)


# In[15]:


str = "PARVEEN bibi"
rslt = str.isdecimal()
print (rslt)

str = "3"
rslt = str.isdecimal()
print (rslt)

str = "7.333"
rslt = str.isdecimal()
print (rslt)


# In[16]:


str = "PARVEEN bibi"
rslt = str.isdigit()
print (rslt)

str = "3"
rslt = str.isdigit()
print (rslt)


# In[17]:


str = "PARVEENbibi"
rslt = str.isidentifier()
print (rslt)

str = "3fgd"
rslt = str.isidentifier()
print (rslt)


# In[18]:


str = "PARVEEN bibi"
rslt = str.islower()
print (rslt)

str = "abc5"
rslt = str.islower()
print (rslt)


# In[19]:


str = "PARVEEN bibi"
rslt = str.isnumeric()
print (rslt)

str = "5"
rslt = str.isnumeric()
print (rslt)


# In[20]:


str = "PARVEEN bibi"
rslt = str.isprintable()
print (rslt)

str = "\n"
rslt = str.isprintable()
print (rslt)


# In[21]:


str = "   PARVEEN   bibi"
rslt = str.isspace()
print (rslt)

str = "        "
rslt = str.isspace()
print (rslt)


# In[22]:


s = 'Python Is Good.'
print(s.istitle())

s = 'Python is good'
print(s.istitle())

s = 'This Is @ Symbol.'
print(s.istitle())

s = '99 Is A Number'
print(s.istitle())

s = 'PYTHON'
print(s.istitle())


# In[23]:


str = "PARVEEN bibi"
rslt = str.isupper()
print (rslt)

str = "ABS5"
rslt = str.isupper()
print (rslt)


# In[24]:


a = {'2', '5', '2'}
s = '-->'
print(s.join(a))

test =  {'2', '7', '3'}
s = ', '
print(s.join(test))

test =  ['2', '3', '3']
s = ', '
print(s.join(test))


# In[25]:


str = "PARVEEN bibi"
fillchar="*"
rslt = str.ljust(20, fillchar)
print (rslt)


# In[26]:


str = "PARVEEN bibi"
rslt = str.lower()
print (rslt)


# In[27]:


str = "      PARVEEN bibi"
rslt = str.lstrip( )
print (rslt)


# In[28]:


str1="abc"
str2="def"
str="abc"
print(str.maketrans(str1,str2))


# In[29]:


str="Python is fun"
print(str.partition("is"))

str="Python is fun"
print(str.partition("not"))


# In[33]:


str="Python is fun"
print(str.replace("is", "isn't"))


# In[31]:


str="Python is is is fun"
print(str.rfind('is'))


# In[34]:


str="Python is is is fun fun"
print(str.rindex('fun'))


# In[35]:


str = "PARVEEN bibi"
fillchar="*"
rslt = str.rjust(20,fillchar)
print (rslt)


# In[36]:


str="Python is fun"
print(str.rpartition("is"))

str="Python is fun"
print(str.rpartition("not"))


# In[37]:


str="Python is fun"
print(str.startswith("is"))

str="Python is fun"
print(str.startswith("P"))


# In[38]:


str="Python is fun"
print(str.title())


# In[39]:


str="Python is fun"
print(str.upper())


# In[40]:


str="Python, is, fun"
print(str.split(','))

str="Python, is, fun"
print(str.split(',', 0))


# In[41]:


str="Python is fun"
print(str.zfill(25))


# In[42]:


str="Python\nis\nfun"
print(str.splitlines())
print(str.splitlines(True))


# In[43]:


str1="abc"
str2="ghi"
str3="c"

str="abcdef"
trans = str.maketrans(str1,str2,str3)

print(str.translate(trans))


# In[44]:


str="    Python is fun      "
print(str.strip())


# In[45]:


str="Python is fun      "
print(str.rstrip())


# In[46]:


str = "PARVEEN bibi"
rslt = str.swapcase()
print (rslt)


# In[ ]:




