#!/usr/bin/env python
# coding: utf-8

# In[1]:


############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
from importlib import reload
from helper import run
import ecc
import helper

from ecc import FieldElement, Point


# ### Exercise 1
# 
# Evaluate whether these points are on the curve \\(y^{2}\\)=\\(x^{3}\\)+7 over \\(F_{223}\\)
# 
# (192,105), (17,56), (200,119), (1,193), (42,99)

# In[2]:


# Exercise 1

prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)

def oncurve(x,y):
    return y**2 == x**3 + a*x + b

print(oncurve(FieldElement(192, prime), FieldElement(105,prime)))
print(oncurve(FieldElement(17, prime), FieldElement(56,prime)))
print(oncurve(FieldElement(200, prime), FieldElement(119,prime)))
print(oncurve(FieldElement(1, prime), FieldElement(193,prime)))
print(oncurve(FieldElement(42, prime), FieldElement(99,prime)))

# result : True True False True False

# (192,105), (17,56), (200,119), (1,193), (42,99)


# In[3]:


from ecc import FieldElement, Point
a = FieldElement(num=0, prime=223)
b = FieldElement(num=7, prime=223)
x = FieldElement(num=192, prime=223)
y = FieldElement(num=105, prime=223)
p1 = Point(x, y, a, b)
print(p1)


# In[4]:


from ecc import FieldElement, Point
prime = 223
a = FieldElement(num=0, prime=prime)
b = FieldElement(num=7, prime=prime)
x1 = FieldElement(num=192, prime=prime)
y1 = FieldElement(num=105, prime=prime)
x2 = FieldElement(num=17, prime=prime)
y2 = FieldElement(num=56, prime=prime)
p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)
print(p1+p2)


# ### Exercise 2
# 
# For the curve \\(y^{2}\\)=\\(x^{3}\\)+7 over \\(F_{223}\\), find:
# 
# * (170,142) + (60,139)
# * (47,71) + (17,56)
# * (143,98) + (76,66)

# In[20]:


# Exercise 2

prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)
p1 = Point(FieldElement(170,prime), FieldElement(142, prime),a,b)
p2 = Point(FieldElement(60, prime), FieldElement(139,prime),a,b)
print(p1 +p2)
# result : Point(220,181)_0_7 FieldElement(223)

p1 = Point(FieldElement(47,prime), FieldElement(71, prime),a,b)
p2 = Point(FieldElement(17, prime), FieldElement(56,prime),a,b)
print(p1 +p2)
# result : Point(215,68)_0_7 FieldElement(223)

p1 = Point(FieldElement(143,prime), FieldElement(98, prime),a,b)
p2 = Point(FieldElement(76, prime), FieldElement(66,prime),a,b)
print(p1 +p2)
# result : Point(47,71)_0_7 FieldElement(223)

# (170,142) + (60,139)
# (47,71) + (17,56)
# (143,98) + (76,66)


# ### Exercise 3
# 
# Extend `ECCTest` to test for the additions from the previous exercise. Call this `test_add`.
# 
# #### Make [this test](/edit/code-ch03/ecc.py) pass: `ecc.py:ECCTest:test_add`

# In[6]:


# Exercise 3

reload(ecc)
run(ecc.ECCTest("test_add"))


# ### Exercise 4
# 
# For the curve \\(y^{2}\\)=\\(x^{3}\\)+7 over \\(F_{223}\\), find:
# 
# * 2⋅(192,105)
# * 2⋅(143,98)
# * 2⋅(47,71)
# * 4⋅(47,71)
# * 8⋅(47,71)
# * 21⋅(47,71)

# In[33]:


# Exercise 4
prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)
x1 = FieldElement(47,  prime)
y1 = FieldElement(71,  prime)
p = Point(x1,y1,a,b)
s = 2

for i in range(1,s+1):
    result = i * p
    p1 = [result.x, result.y,result.a.num,result.b.num]
print(p1)
    
# 2*(192, 105)
# result : [49, 71, 0, 7]

# 2*(143, 98)
# result : [64, 168, 0, 7]

# 2*(47, 71)
# result : [36, 111, 0, 7]

# 4*(47, 71)
# result : [194, 51, 0, 7]

# 8*(47, 71)
# result : [116, 55, 0, 7]

# 21*(47, 71)
# result : [None, None, 0, 7]


# create a product variable
# add the point to the product n times
# print the product


# In[34]:


from ecc import FieldElement, Point
import math
prime = 223
re = []
a = FieldElement(0, prime)
b = FieldElement(7, prime)
x = FieldElement(47, prime)
y = FieldElement(71, prime)
p = Point(x, y, a, b)

print("Forward direction")
for i in range(1,21):
    result = i * p
    p1 = [result.x.num, result.y.num,result.a.num,result.b.num]
    re.append(p1)
    print(p1)
# result : Forward direction
# [47, 71, 0, 7]
# [36, 111, 0, 7]
# [15, 137, 0, 7]
# [194, 51, 0, 7]
# [126, 96, 0, 7]
# [139, 137, 0, 7]
# [92, 47, 0, 7]
# [116, 55, 0, 7]
# [69, 86, 0, 7]
# [154, 150, 0, 7]
# [154, 73, 0, 7]
# [69, 137, 0, 7]
# [116, 168, 0, 7]
# [92, 176, 0, 7]
# [139, 86, 0, 7]
# [126, 127, 0, 7]
# [194, 172, 0, 7]
# [15, 86, 0, 7]
# [36, 112, 0, 7]
# [47, 152, 0, 7]

# Try Solving inverse direction discrete point division 
# Discrete Log Problem,  logPQ = 7
# The log equation on the left has no analytically calculable algorithm.
# So could not solve. :(


# ### Exercise 5
# 
# For the curve \\(y^{2}\\)=\\(x^{3}\\)+7 over \\(F_{223}\\), find the order of the group generated by (15,86)

# In[37]:


# Exercise 5

# if point find point at infinity the order of group
prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)
x = FieldElement(15, prime)
y = FieldElement(86, prime)
p = Point(x, y, a, b)
inf = Point(None, None, a, b)
product = p
count = 1

while product != inf:
    product += p
    count += 1

print(count)

# result : 7


# In[10]:


from ecc import FieldElement, Point
prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)
x = FieldElement(15, prime)
y = FieldElement(86, prime)
p = Point(x, y, a, b)
print(7*p)


# In[11]:


gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
p = 2**256 - 2**32 - 977
print(gy**2 % p == (gx**3 + 7) % p)


# In[12]:


from ecc import FieldElement, Point
gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
p = 2**256 - 2**32 - 977
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
x = FieldElement(gx, p)
y = FieldElement(gy, p)
seven = FieldElement(7, p)
zero = FieldElement(0, p)
G = Point(x, y, zero, seven)
print(n*G)


# In[13]:


from ecc import G, N
print(N*G)


# In[14]:


from ecc import S256Point, G, N
z = 0xbc62d4b80d9e36da29c16c5d4d9f11731f36052c72401a76c23c0fb5a9b74423
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
px = 0x04519fac3d910ca7e7138f7013706f619fa8f033e6ec6e09370ea38cee6a7574
py = 0x82b51eab8c27c66e26c858a079bcdf4f1ada34cec420cafc7eac1a42216fb6c4
point = S256Point(px, py)
s_inv = pow(s, N-2, N)
u = z * s_inv % N
v = r * s_inv % N
print((u*G + v*point).x.num == r)


# ### Exercise 6
# 
# Verify whether these signatures are valid:
# 
# ```
# P = (0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c,
# 0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34)
# 
# # signature 1
# z = 0xec208baa0fc1c19f708a9ca96fdeff3ac3f230bb4a7ba4aede4942ad003c0f60
# r = 0xac8d1c87e51d0d441be8b3dd5b05c8795b48875dffe00b7ffcfac23010d3a395
# s = 0x68342ceff8935ededd102dd876ffd6ba72d6a427a3edb13d26eb0781cb423c4
# 
# # signature 2
# z = 0x7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
# r = 0xeff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c
# s = 0xc7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6
# ```

# In[38]:


# Exercise 6
# Verify whether these signatures are valid

from ecc import S256Point, N, G
point = S256Point(
    0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c, 
    0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34)
# signature 1
z = 0xec208baa0fc1c19f708a9ca96fdeff3ac3f230bb4a7ba4aede4942ad003c0f60
r = 0xac8d1c87e51d0d441be8b3dd5b05c8795b48875dffe00b7ffcfac23010d3a395
s = 0x68342ceff8935ededd102dd876ffd6ba72d6a427a3edb13d26eb0781cb423c4
u = z * pow(s, N-2, N) % N
v = r * pow(s, N-2, N) % N
print((u * G + v * point).x.num == r)
# result : True

# signature 2
z = 0x7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
r = 0xeff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c
s = 0xc7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6
u = z * pow(s, N-2, N) % N
v = r * pow(s, N-2, N) % N
print((u * G + v * point).x.num == r)
# result : True


# In[16]:


from ecc import S256Point, G, N
from helper import hash256
e = int.from_bytes(hash256(b'my secret'), 'big')
z = int.from_bytes(hash256(b'my message'), 'big')
k = 1234567890
r = (k*G).x.num
k_inv = pow(k, N-2, N)
s = (z+r*e) * k_inv % N
point = e*G
print(point)
print(hex(z))
print(hex(r))
print(hex(s))


# ### Exercise 7
# 
# Sign the following message with the secret
# 
# ```
# e = 12345
# z = int.from_bytes(hash256('Programming Bitcoin!'), 'big')
# ```

# In[42]:


# Exercise 7
# Sign the following message with the secret

from ecc import S256Point, G, N
from helper import hash256
# Exercise 7

e = 12345
z = int.from_bytes(hash256(b'Programming Bitcoin!'), 'big')
# choose a random k
k = 1234
# calculate r (kG's x-coordinate)
r = (k * G).x.num
k_inv = pow(k, N-2, N)
# calculate s ((z+re)/k)
s = (z + r*e) * k_inv % N
print(e*G)
# result : S256Point(f01d6b9018ab421dd410404cb869072065522bf85734008f105cf385a023a80f, 0eba29d0f0c5408ed681984dc525982abefccd9f7ff01dd26da4999cf3f6a295)

print(hex(z))
# result : 0x969f6056aa26f7d2795fd013fe88868d09c9f6aed96965016e1936ae47060d48

print(hex(r))
# result : 0xe37648435c60dcd181b3d41d50857ba5b5abebe279429aa76558f6653f1658f2

print(hex(s))
# result : 0xcb2f32a39c80daf3b767c4282f4a271172747ee2b19db13dc0218f6ec9b92582


# In[ ]:




