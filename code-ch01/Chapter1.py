#!/usr/bin/env python
# coding: utf-8

# In[1]:


############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
from importlib import reload
from helper import run
import ecc
import helper

from ecc import FieldElement


# In[2]:


from ecc import FieldElement
a = FieldElement(7, 13)
b = FieldElement(6, 13)
print(a == b)
print(a == a)


# ### Exercise 1
# 
# Write the corresponding method `__ne__` which checks if two `FieldElement` objects are _not equal_ to each other.
# 
# #### Make [this test](/edit/code-ch01/ecc.py) pass: `ecc.py:FieldElementTest:test_ne`

# In[ ]:


# Exercise 1

reload(ecc)
run(ecc.FieldElementTest("test_ne"))


# In[ ]:


print(7 % 3)


# In[ ]:


print(-27 % 13)


# ### Exercise 2
# 
# Solve these problems in \\(F_{57}\\) (assume all +'s here are \\(+_{f}\\) and -`s here \\(-_{f}\\))
# 
# * 44+33
# * 9-29
# * 17+42+49
# * 52-30-38

# In[ ]:


# Exercise 2

# remember that % is the modulo operator
prime = 57
# 44+33
# 9-29
# 17+42+49
# 52-30-38


# In[ ]:


from ecc import FieldElement
a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)
print(a+b==c)


# ### Exercise 3
# 
# Write the corresponding `__sub__` method which defines the subtraction of two `FieldElement` objects.
# 
# #### Make [this test](/edit/code-ch01/ecc.py) pass: `ecc.py:FieldElementTest:test_sub`

# In[ ]:


# Exercise 3

reload(ecc)
run(ecc.FieldElementTest("test_sub"))


# ### Exercise 4
# 
# Solve the following equations in \\(F_{97}\\) (again, assume ⋅ and exponentiation are field versions):
# 
# * 95⋅45⋅31
# * 17⋅13⋅19⋅44
# * \\(12^{7}\\)⋅\\(77^{49}\\)

# In[ ]:


# Exercise 4

prime = 97

# 95*45*31
# 17*13*19*44
# 12**7*77**49


# ### Exercise 5
# 
# For k = 1, 3, 7, 13, 18, what is this set in \\(F_{19}\\)?
# 
# {k⋅0, k⋅1, k⋅2, k⋅3, ... k⋅18}
# 
# Do you notice anything about these sets?

# In[ ]:


# Exercise 5

prime = 19
k = 1  # 3, 7, 13 and 18 are the other possibilities
# loop through all possible k's 0 up to prime-1
# calculate k*iterator % prime

# Hint - sort!


# In[ ]:


from ecc import FieldElement
a = FieldElement(3, 13)
b = FieldElement(12, 13)
c = FieldElement(10, 13)
print(a*b==c)


# ### Exercise 6
# 
# Write the corresponding `__mul__` method which defines the multiplication of two Finite Field elements.
# 
# #### Make [this test](/edit/code-ch01/ecc.py) pass: `ecc.py:FieldElementTest:test_mul`

# In[ ]:


# Exercise 6

reload(ecc)
run(ecc.FieldElementTest("test_mul"))


# In[ ]:


from ecc import FieldElement
a = FieldElement(3, 13)
b = FieldElement(1, 13)
print(a**3==b)


# ### Exercise 7
# 
# For p = 7, 11, 17, 31, what is this set in \\(F_{p}\\)?
# 
# {\\(1^{(p-1)}\\), \\(2^{(p-1)}\\), \\(3^{(p-1)}\\), \\(4^{(p-1)}\\), ... \\((p-1)^{(p-1)}\\)}

# In[ ]:


# Exercise 7

primes = [7, 11, 17, 31, 43]


# ### Exercise 8
# 
# Solve the following equations in \\(F_{31}\\):
# 
# * 3 / 24
# * \\(17^{-3}\\)
# * \\(4^{-4}\\)⋅11

# In[ ]:


# Exercise 8

# 3/24
# 17**-3
# 4**-4*11


# ### Exercise 9
# 
# Write the corresponding `__truediv__` method which defines the division of two field elements.
# 
# Note that in Python3, division is separated into `__truediv__` and `__floordiv__`. The first does normal division, the second does integer division.
# 
# #### Make [this test](/edit/code-ch01/ecc.py) pass: `ecc.py:FieldElementTest:test_div`

# In[ ]:


# Exercise 9

reload(ecc)
run(ecc.FieldElementTest("test_div"))


# In[ ]:


from ecc import FieldElement
a = FieldElement(7, 13)
b = FieldElement(8, 13)
print(a**-3==b)

