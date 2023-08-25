from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

import hashlib
hash_object = hashlib.sha256(b'Password1234')
hex_dig = hash_object.digest()
print(hex_dig)

key = hex_dig
iv = hex_dig[0:16]


cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
decryptor=cipher.decryptor()
BUF_SIZE = 1024 # Read file in 32kb chunks


fileName="test.enc"
decFile="test_dec.txt"
f1 = open(decFile, 'wb')
with open(fileName, 'rb') as f2:
    while True:
        data = f2.read(BUF_SIZE)
        if (len(data)>0):
            pt = decryptor.update(data)
            f1.write(pt)
        else:
            break

f2.close()
f1.close()
