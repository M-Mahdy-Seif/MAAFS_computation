# The 256-bit hash function
from Crypto.Hash import SHA256

# The HMAC function
from Crypto.Hash import HMAC
import hashlib


# The Advanced Encryption System  CBC Mode(Symmetric Encryption)
from Crypto.Cipher import AES
from Crypto import Random

#The random number generation
import os

# The public key encrypton (RSA)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# The bilinear pairing
from bplib import bp

# The elliptic curve
from fastecdsa.curve import P256
from fastecdsa.point import Point

#Modular Operation
from mod import Mod

# The AES encryption procedures
key = b'Sixteen byte key'
print (key)
iv = Random.new().read(AES.block_size)
print (iv)

aes = AES.new(key, AES.MODE_CBC, iv)
data = b'hello world 1234' # <- 16 bytes
encd = aes.encrypt(data)
print (encd)

adec = AES.new(key, AES.MODE_CBC, iv)
decd = adec.decrypt(encd)
print (decd)



                 

# The hash function
h = SHA256.new()
h.update(b'Hello')
digest=h.hexdigest()
print (digest)
                 
                 
# The HMAC function (MD5)
print('The HMAC')
secret = b'Swordfish'
h = HMAC.new(secret,b'Hello',SHA256)
#h.update(b'Hello')
digestHMAC=h.hexdigest()
print(digestHMAC)


#The random number generation
random = os.urandom(16)
print(random)


# Generating the public key
keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
#pubKeyPEM = pubKey.exportKey()
#print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
#privKeyPEM = keyPair.exportKey()
#print(privKeyPEM.decode('ascii'))

# The encryption of RSA
msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))

# The decryption of RSA
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)

# The exponential operation
print('The exponential operation')
a = 2988348162058574136915891421498819466320163312926952423791023078876139
b = 2351399303373464486466122544523690094744975233415544072992656881240319
m = 10 ** 40
print(pow(a, b, m))




# The bilinear pairing
G = bp.BpGroup()
g1, g2 = G.gen1(), G.gen2()
gt = G.pair(g1, g2)
# The exponentiation operation
gt6 = gt**6
print('The bilinear check')
result1 = G.pair(g1, 6*g2) == gt6
print(result1)
result2 = G.pair(6*g1, g2) == gt6
print(result2)
result3 = G.pair(2*g1, 3*g2) == gt6
print(result3)


# The elliptic curve operations
xs = 0xde2444bebc8d36e682edd27e0f271508617519b3221a8fa0b77cab3989da97c9
ys = 0xc093ae7ff36e5380fc01a5aad1e66659702de80f53cec576b6350b243042a256
S = Point(xs, ys, curve=P256)

print ('The S point')
print (S)

xt = 0x55a8b00f8da1d44e62f6b3b25316212e39540dc861c89575bb8cf92e35e0986b
yt = 0x5421c3209c2d6c704835d82ac4c3dd90f61a8a52598b9e7ab656e9d8c8b24316
T = Point(xt, yt, curve=P256)

print ('The T point')
print(T)

# Point Addition
R = S + T
print ('The addition result:')
print(R)

# Point Subtraction: (xs, ys) - (xt, yt) = (xs, ys) + (xt, -yt)
R = S - T
print ('The subtraction:')
print(R)

# Point Doubling
R = S + S  # produces the same value as the operation below
R = 2 * S  # S * 2 works fine too i.e. order doesn't matter

d = 0xc51e4753afdec1e6b6c6a5b992f43f8dd0c7a8933072708b6522468b2ffb06fd

# Scalar Multiplication
R = d * S  # S * d works fine too i.e. order doesn't matter

e = 0xd37f628ece72a462f0145cbefe3f0b355ee8332d37acdd83a358016aea029db7

# Joint Scalar Multiplication
R = d * S + e * T


#Modular multiplication 
z= 0xc51e4753afdec1e6b6c6a5b992f43f8dd0c7
print(Mod(z*3,10))

#Modular addition 
z= 0xc51e4753afdec1e6b6c6a5b992f43f8dd0c7
print(Mod(z+z,10))