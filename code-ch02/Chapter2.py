#!/usr/bin/env python
# coding: utf-8

# In[1]:


############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
from importlib import reload
from helper import run
import ecc
import helper

from ecc import Point


# In[2]:


from ecc import Point
p1 = Point(-1, -1, 5, 7)
p2 = Point(-1, -2, 5, 7)


# ### Exercise 1
# 
# Determine which of these points are on the curve \\(y^{2}\\)=\\(x^{3}\\)+5x+7:
# 
# (2,4), (-1,-1), (18,77), (5,7)

# In[7]:


# Exercise 1

# (2,4), (-1,-1), (18,77), (5,7)

def on_curve(x,y):
    return y**2 == x**3 + 5*x +7

print(on_curve(2,4))

print(on_curve(-1,-1))

print(on_curve(18,77))

print(on_curve(5,7))
# equation in python is: y**2 == x**3 + 5*x + 7

# result : False True True False


# ### Exercise 2
# 
# Write the `__ne__` method for `Point`.
# 
# #### Make [this test](/edit/code-ch02/ecc.py) pass: `ecc.py:PointTest:test_ne`

# In[8]:


# Exercise 2

reload(ecc)
run(ecc.PointTest("test_ne"))


# In[36]:


from ecc import Point
p1 = Point(-1, -1, 5, 7)
p2 = Point(-1, 1, 5, 7)
inf = Point(None, None, 5, 7)

def __ne__(self, other):
    return not (self == other)

print(__ne__(p1,inf))
print(p1 + inf)

print(__ne__(inf,p2))
print(inf + p2)

print(__ne__(p1,p2))
print(p1+p2)

# result : True Point(-1,-1)_5_7 True Point(-1,1)_5_7 True

### Exercise 3

Handle the case where the two points are additive inverses. That is, they have the same `x`, but a different `y`, causing a vertical line. This should return the point at infinity.

#### Make [this test](/edit/code-ch02/ecc.py) pass: `ecc.py:PointTest:test_add0`
# In[41]:


# Exercise 3
from ecc import Point

def __init__(self, x, y, a, b):
    
    self.a = a
    self.b = b
    self.x = x
    self.y = y
    if self.x is None and self.y is None:
        return
        if self.y**2 != self.x**3 + a * x + b:  
            raise ValueError('({}, {}) is not on the curve'.format(x, y))

p1 = __init__(1,1,1,7)
p2 = __init__(1,-1,1,7)

def __add__(self, other): 
    
    if self.a != other.a or self.b != other.b:
        raise TypeError('Points {}, {} are not on the same curve'.format
        (self, other))
    if self.x is None:
        return other
    if other.x is None: 
        return self
    
print(__add__(p1,p2))
# Case 1: self.x == other.x, self.y != other.y
# Handle the case where the two points are additive inverses (that is, they have the same `x` but a different `y`, causing a vertical line). This should return the point at infinity.


# ### Exercise 4
# 
# For the curve \\(y^{2}\\)=\\(x^{3}\\)+5x+7, what is (2,5) + (-1,-1)?

# In[1]:


# Exercise 4
# Deriving the Point Addition Formula
from ecc import Point

a = 5
b = 7
# y^2 = x^3 + 5x + 7
x1, y1 = 2, 5
x2, y2 = -1, -1
s = (y2 - y1) / (x2 - x1)

# Vuera's formula
x3 = s ** 2 - x1 -x2
y3 = s * (x1 - x3) - y1
print(x3 , y3)

# result : 3.0 -7.0

# (x1,y1) + (x2,y2)


# ### Exercise 5
# 
# Write the `__add__` method where \\(x_{1}\\)≠\\(x_{2}\\)
# 
# #### Make [this test](/edit/code-ch02/ecc.py) pass: `ecc.py:PointTest:test_add1`

# In[2]:


# Exercise 5

# if x1 ≠ x2

def __add__(self, other):
    if self.a != other.a or self.b != other.b:
        raise TypeError
    if self.x is None:
        return other
    if other.x is None:
        return self
    if self.x != other.x:
        s = (other.y - self.y) / (other.x - self.x)
        x = s**2 - self.x - other.x
        y = s * (self.x - x) - self.y
        return  self.__class__(None, None, self.a, self.b)
    
reload(ecc)
run(ecc.PointTest("test_add1"))


# ### Exercise 6
# 
# For the curve \\(y^{2}\\)=\\(x^{3}\\)+5x+7, what is (-1,-1) + (-1,-1)?

# In[3]:


# Exercise 6

from ecc import Point

# if the curve y^2 = x^3 + 5x +7
# if P1 = P2
# Deriving the Point Addition Formula

a = 5
b = 7
x1, y1 = -1, -1

s = (3 * x1**2 + a) / (2 * y1)
x3 = s**2 - 2 * x1
y3 = s * (x1 - x3) - y1
print(x3,y3)

# (-1,-1) + (-1,-1)


# ### Exercise 7
# 
# Write the `__add__` method when \\(P_{1}\\)=\\(P_{2}\\).
# 
# #### Make [this test](/edit/code-ch02/ecc.py) pass: `ecc.py:PointTest:test_add2`

# In[4]:


# Exercise 7
# if x1 = x2
# Deriving the Point Addition Formula

def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError
        if self.x is None:
            return other
        if other.x is None:
            return self
        if self == other:
            s = (3 * self.x**2 + self.a) / (2 * self.y)
            x = s**2 - 2 * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)
reload(ecc)
run(ecc.PointTest("test_add2"))


# In[ ]:




