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

# In[3]:


# Exercise 1

reload(ecc)
run(ecc.FieldElementTest("test_ne"))


# In[4]:


print(7 % 3)

def __ne__(self, other):
    return not (self == other)

__ne__(7, 3)

# result : 1 True


# In[5]:


print(-27 % 13)
__ne__(-27,13)

# result : 12 True


# ### Exercise 2
# 
# Solve these problems in \\(F_{57}\\) (assume all +'s here are \\(+_{f}\\) and -`s here \\(-_{f}\\))
# 
# * 44+33
# * 9-29
# * 17+42+49
# * 52-30-38

# In[6]:


# Exercise 2

# remember that % is the modulo operator
prime = 57

# 44+33
print((44+33)%57)

# 9-29
print((9-29)%57)

# 17+42+49
print((17+42+49)%57)

# 52-30-38
print((52-30-38)%57)

# result : 20 37 51 41


# In[7]:


from ecc import FieldElement
a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)
print(a+b==c)
# result : True


# ### Exercise 3
# 
# Write the corresponding `__sub__` method which defines the subtraction of two `FieldElement` objects.
# 
# #### Make [this test](/edit/code-ch01/ecc.py) pass: `ecc.py:FieldElementTest:test_sub`

# In[8]:


# Exercise 3

reload(ecc)
run(ecc.FieldElementTest("test_sub"))


# In[9]:


from ecc import FieldElement

def __sub__(self, other):
    if self.prime != other.prime:
        raise TypeError('Cannot subtract two numbers in different Fields')
    num = (self.num - other.num) % self.prime
    return self.__class__(num, self.prime)

a = FieldElement(5, 13)
b = FieldElement(12,13)

__sub__(a,b)

# result : FieldElement_13(6)


# ### Exercise 4
# 
# Solve the following equations in \\(F_{97}\\) (again, assume ⋅ and exponentiation are field versions):
# 
# * 95⋅45⋅31
# * 17⋅13⋅19⋅44
# * \\(12^{7}\\)⋅\\(77^{49}\\)

# In[10]:


# Exercise 4

prime = 97

# 95*45*31
print((95*45*31)%97)

# 17*13*19*44
print((17*13*19*44)%97)

# 12**7*77**49
print(((12**7)*(19**44))%97)

# result : 23 68 27


# ### Exercise 5
# 
# For k = 1, 3, 7, 13, 18, what is this set in \\(F_{19}\\)?
# 
# {k⋅0, k⋅1, k⋅2, k⋅3, ... k⋅18}
# 
# Do you notice anything about these sets?

# In[11]:


# Exercise 5

prime = 19
k = 20  # 1, 3, 7, 13 and 18 are the other possibilities
h = []
for i in range (0,19):
    h.append((i*k)%19)
    h.sort()
print(h)

# result : if k = 1, 3 , 7, 13, 18 same outcome


# In[12]:


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

def __mul__(self, other):
    if self.prime != other.prime:
        raise TypeError('Cannot multiply two numbers in different Fields')
    num = (self.num * other.num) % self.prime
    return self.__class__(num, self.prime)

print(a**3 == b)


# ### Exercise 7
# 
# For p = 7, 11, 17, 31, what is this set in \\(F_{p}\\)?
# 
# {\\(1^{(p-1)}\\), \\(2^{(p-1)}\\), \\(3^{(p-1)}\\), \\(4^{(p-1)}\\), ... \\((p-1)^{(p-1)}\\)}

# In[ ]:


# Exercise 7

primes = [7, 11, 17, 31, 43]
ps = []

for i in range (0,len(primes)):
    for j in range(1,primes[i]):
        ps.append((j**primes[i])%primes[i])
    print(ps)

""" 
 result : [1, 2, 3, 4, 5, 6]
 [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
 [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
 [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
 Therefore, elements are output as much as order-1.
"""


# ### Exercise 8
# 
# Solve the following equations in \\(F_{31}\\):
# 
# * 3 / 24
# * \\(17^{-3}\\)
# * \\(4^{-4}\\)⋅11

# In[43]:


# Exercise 8

prime = 31


def __pow(self, division):
    return (self * (division**(prime-2)))%prime

# 3/24
print(__pow(3,24))

# 17**-3
def __pow__(self,negative_exponent):
    n = negative_exponent
    while n < 0:
        n += prime -1
    num = pow(self, n, prime)
    return num

print(__pow__(17,-3))

# 4**-4*11
print(__pow__(4,-4*11))

# result : 4 29 4


# Fermat's Little Thorem Applications
# There are many proofs of this theorem, but perhaps the simplest is using what we saw in Exercise 5—namely, that these sets are equal:
# {1, 2, 3, ... p–2, p–1} = {n%p, 2n%p, 3n%p (p–2)n%p, (p–1)n%p}
# The resulting numbers might not be in the right order, but the same numbers are in
# both sets. We can then multiply every element in both sets to get this equality: 1 ⋅ 2 ⋅ 3 ⋅ ... ⋅ (p–2) ⋅ (p–1) % p = n ⋅ 2n ⋅ 3n ⋅ ... ⋅ (p–2)n ⋅ (p–1)n % p
# The left side is the same as (p–1)! % p where ! is the factorial (e.g., 5! = 5 ⋅ 4 ⋅ 3 ⋅ 2 ⋅ 1). On the right side, we can gather up all the n`’s and get:
# (p–1)! ⋅ n(p–1) % p Thus:
# (p–1)! % p = (p–1)! ⋅ n(p–1) % p
# The (p–1)! on both sides cancel, giving us:
# 1 = n(p–1) % p
# This proves Fermat’s little theorem


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

