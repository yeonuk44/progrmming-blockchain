#!/usr/bin/env python
# coding: utf-8

# In[ ]:


############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
from importlib import reload
from helper import run
import ecc
import helper


# ### Exercise 1
# 
# Find the uncompressed SEC format for the Public Key where the Private Key secrets are:
# 
# * 5000
# * \\(2018^{5}\\)
# * 0xdeadbeef12345

# In[ ]:


# Exercise 1

from ecc import PrivateKey

# 5000
# 2018**5
# 0xdeadbeef12345
# privatekey.point is the public key for a private key


# ### Exercise 2
# 
# Find the Compressed SEC format for the Public Key where the Private Key secrets are:
# 
# * 5001
# * \\(2019^{5}\\)
# * 0xdeadbeef54321

# In[ ]:


# Exercise 2

from ecc import PrivateKey

# 5001
# 2019**5
# 0xdeadbeef54321


# ### Exercise 3
# 
# Find the DER format for a signature whose `r` and `s` values are:
# 
# * r =
# 
# `0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6`
# 
# * s =
# 
# `0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec`

# In[ ]:


# Exercise 3

from ecc import Signature

r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec


# ### Exercise 4
# 
# Convert the following hex to binary and then to Base58:
# 
# * `7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d`
# * `eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c`
# * `c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6`

# In[ ]:


# Exercise 4

from helper import encode_base58

# 7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
# eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c
# c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6


# ### Exercise 5
# 
# Find the address corresponding to Public Keys whose Private Key secrets are:
# 
# * 5002 (use uncompressed SEC, on testnet)
# * \\(2020^{5}\\) (use compressed SEC, on testnet)
# * 0x12345deadbeef (use compressed SEC on mainnet)

# In[ ]:


# Exercise 5

from ecc import PrivateKey

# 5002 (use uncompressed SEC, on testnet)
# 2020**5 (use compressed SEC, on testnet)
# 0x12345deadbeef (use compressed SEC on mainnet)


# ### Exercise 6
# 
# Find the WIF for Private Key whose secrets are:
# 
# * 5003 (compressed, testnet)
# * \\(2021^{5}\\) (uncompressed, testnet)
# * 0x54321deadbeef (compressed, mainnet)

# In[ ]:


# Exercise 6

from ecc import PrivateKey

# 5003
# 2021**5
# 0x54321deadbeef


# ### Exercise 7
# 
# Write a function `little_endian_to_int` which takes Python bytes, interprets those bytes in Little-Endian and returns the number.
# 
# #### Make [this test](/edit/code-ch04/helper.py) pass: `helper.py:HelperTest:test_little_endian_to_int`

# In[ ]:


# Exercise 7

reload(helper)
run(helper.HelperTest("test_little_endian_to_int"))


# ### Exercise 8
# 
# Write a function `int_to_little_endian` which does the reverse of the last exercise.
# 
# #### Make [this test](/edit/code-ch04/helper.py) pass: `helper.py:HelperTest:test_int_to_little_endian`

# In[ ]:


# Exercise 8

reload(helper)
run(helper.HelperTest("test_int_to_little_endian"))


# ### Exercise 9
# 
# Create a testnet address for yourself using a long secret that only you know. This is important as there are bots on testnet trying to steal testnet coins. Make sure you write this secret down somewhere! You will be using the secret later to sign Transactions.

# In[ ]:


# Exercise 9

from ecc import PrivateKey
from helper import hash256, little_endian_to_int

# select a passphrase here, add your email address into the passphrase for security
# passphrase = b'your@email.address some secret only you know'
# secret = little_endian_to_int(hash256(passphrase))
# create a private key using your secret
# print an address from the public point of the private key with testnet=True

