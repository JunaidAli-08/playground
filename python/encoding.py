#encoding * decoding

# import base64
# name = b"My name is "
# c=base64.b64encode(name)
# d= base64.b64decode(c)
# print(d.decode())

###hashlib####

import hashlib
b=hashlib.sha256()
b.update(b"Junaid@0814")
digest_value=b.digest().hex()
print(digest_value) 

hash2=hashlib.sha256()
hash2.update(b"JunAid@0814")
digest_value1=hash2.digest().hex()
print(digest_value1)

import base64
name=b"Junaid"
c=base64.b64encode(name)
print(c)
d=base64.b64decode(c)
print(d)
