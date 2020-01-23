#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

# In[2]:


# Exercise 1
# Find 'the uncompressed SEC' format for the Public Key where the Private Key secrets
from ecc import PrivateKey

#5000
priv = PrivateKey(5000)
print(priv.point.sec(compressed = False).hex()) #uncompressed
# result : 04ffe558e388852f0120e46af2d1b370f85854a8eb0841811ece0e3e03d282d57c315dc72890a4f10a1481c031b03b351b0dc79901ca18a00cf009dbdb157a1d10

# 2018**5
priv = PrivateKey(pow(2018,5))
print(priv.point.sec(compressed = False).hex())
# result : 04027f3da1918455e03c46f659266a1bb5204e959db7364d2f473bdf8f0a13cc9dff87647fd023c13b4a4994f17691895806e1b40b57f4fd22581a4f46851f3b06

# 0xdeadbeef12345
priv = PrivateKey(0xdeadbeef12345)
print(priv.point.sec(compressed = False).hex())
# result : 04d90cd625ee87dd38656dd95cf79f65f60f7273b67d3096e68bd81e4f5342691f842efa762fd59961d0e99803c61edba8b3e3f7dc3a341836f97733aebf987121

# privatekey.point is the public key for a private key


# ### Exercise 2
# 
# Find the Compressed SEC format for the Public Key where the Private Key secrets are:
# 
# * 5001
# * \\(2019^{5}\\)
# * 0xdeadbeef54321

# In[3]:


# Exercise 2
# Find 'the Compressed SEC' format for the Public Key where the Private Key secrets
from ecc import PrivateKey

# 5001
priv = PrivateKey(5001)
print(priv.point.sec(compressed = True).hex()) # compressed
# result : 0357a4f368868a8a6d572991e484e664810ff14c05c0fa023275251151fe0e53d1

# 2019**5
priv = PrivateKey(pow(2019,5))
print(priv.point.sec(compressed = True).hex()) # compressed
# result : 02933ec2d2b111b92737ec12f1c5d20f3233a0ad21cd8b36d0bca7a0cfa5cb8701

# 0xdeadbeef54321
priv = PrivateKey(0xdeadbeef54321)
print(priv.point.sec(compressed = True).hex()) # compressed
# result : 02933ec2d2b111b92737ec12f1c5d20f3233a0ad21cd8b36d0bca7a0cfa5cb8701

# as a result, It shows a marked difference in length compared to the uncompressed format.


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

# In[4]:


# Exercise 3
# Find 'the DER' format for a signature whose `r` and `s` values

from ecc import Signature

r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
sig = Signature(r,s)
print(sig.der().hex())

# result : 3045022037206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c60221008ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec


# ### Exercise 4
# 
# Convert the following hex to binary and then to Base58:
# 
# * `7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d`
# * `eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c`
# * `c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6`

# In[5]:


# Exercise 4
# Convert the following hex to binary and then to Base58

from helper import encode_base58
# 7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
h = '7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d'
print(encode_base58(bytes.fromhex(h)))
# result : 9MA8fRQrT4u8Zj8ZRd6MAiiyaxb2Y1CMpvVkHQu5hVM6

# eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c
h = 'eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c'
print(encode_base58(bytes.fromhex(h)))
# result : 4fE3H2E6XMp4SsxtwinF7w9a34ooUrwWe4WsW1458Pd

# c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6
h = 'c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6'
print(encode_base58(bytes.fromhex(h)))
# result : EQJsjkd6JaGwxrjEhfeqPenqHwrBmPQZjJGNSCHBkcF7



# ### Exercise 5
# 
# Find the address corresponding to Public Keys whose Private Key secrets are:
# 
# * 5002 (use uncompressed SEC, on testnet)
# * \\(2020^{5}\\) (use compressed SEC, on testnet)
# * 0x12345deadbeef (use compressed SEC on mainnet)

# In[6]:


# Exercise 5
# Find the address of bitcoin(use the testnet) corresponding to Public Keys whose Private Key

from ecc import PrivateKey

# 5002 (use uncompressed SEC, on testnet)
priv = PrivateKey(5002)
print(priv.point.address(compressed = False, testnet = True))
# result : mmTPbXQFxboEtNRkwfh6K51jvdtHLxGeMA

# 2020**5 (use compressed SEC, on testnet)
priv = PrivateKey(pow(2020,5))
print(priv.point.address(compressed = False, testnet = True))
# result : muC5h84joNRi2Aiw1FzvS9RkPEXGwaoxGE

# 0x12345deadbeef (use compressed SEC on mainnet)
priv = PrivateKey(0x12345deadbeef)
print(priv.point.address(compressed = False, testnet = True))
# result : mg2MoJnGVV7JKFEawp6zKrKL6gDsoXJJRA


# ### Exercise 6
# 
# Find the WIF for Private Key whose secrets are:
# 
# * 5003 (compressed, testnet)
# * \\(2021^{5}\\) (uncompressed, testnet)
# * 0x54321deadbeef (compressed, mainnet)

# In[9]:


# Exercise 6
# Find the WIF for Private Key whose secrets

from ecc import PrivateKey

# 5003
priv = PrivateKey(5003)
print(priv.wif(compressed = True, testnet = True))
# result : cMahea7zqjxrtgAbB7LSGbcQUr1uX1ojuat9jZodMN8rFTv2sfUK

# 2021**5
priv = PrivateKey(pow(2021,5))
print(priv.wif(compressed = True, testnet = True))
# result : cMahea7zqjxrtgAbB7LSGbcQUr1uX1ojuatBzfkxoXKspfwie91W

# 0x54321deadbeef
priv = PrivateKey(0x54321deadbeef)
print(priv.wif(compressed = True, testnet = True))
# result : cMahea7zqjxrtgAbB7LSGbcQUr1uX1ojuat9qKrpR8M8odsZpvec


# ### Exercise 7
# 
# Write a function `little_endian_to_int` which takes Python bytes, interprets those bytes in Little-Endian and returns the number.
# 
# #### Make [this test](/edit/code-ch04/helper.py) pass: `helper.py:HelperTest:test_little_endian_to_int`

# In[10]:


# Exercise 7
# Write a function little_endian_to_int which takes Python bytes, interprets those bytes in Little-Endian and returns the number.
reload(helper)
run(helper.HelperTest("test_little_endian_to_int"))

def little_endian_to_int(b):
    return int.from_bytes(b, 'little')

# little_endian_to_int takes byte sequence as a little-endian number.
# Returns an integer


# ### Exercise 8
# 
# Write a function `int_to_little_endian` which does the reverse of the last exercise.
# 
# #### Make [this test](/edit/code-ch04/helper.py) pass: `helper.py:HelperTest:test_int_to_little_endian`

# In[ ]:


# Exercise 8
# Write a function int_to_little_endian which does the reverse of the last exercise.

reload(helper)
run(helper.HelperTest("test_int_to_little_endian"))

def int_to_little_endian(n, length):
    return n.to_bytes(length, 'little')

# endian_to_little_endian takes an integer and returns the little-endian
# byte sequence of length


# ### Exercise 9
# 
# Create a testnet address for yourself using a long secret that only you know. This is important as there are bots on testnet trying to steal testnet coins. Make sure you write this secret down somewhere! You will be using the secret later to sign Transactions.

# In[15]:


# Exercise 9

from ecc import PrivateKey
from helper import hash256, little_endian_to_int
passphrase = b'yeonuk44@gmail.com'
secret = little_endian_to_int(hash256(passphrase))
priv = PrivateKey(secret)
print(priv.point.address(testnet=True))
# select a passphrase here, add your email address into the passphrase for security
# passphrase = b'your@email.address some secret only you know'
# secret = little_endian_to_int(hash256(passphrase))
# create a private key using your secret
# print an address from the public point of the private key with testnet=True


# In[ ]:




