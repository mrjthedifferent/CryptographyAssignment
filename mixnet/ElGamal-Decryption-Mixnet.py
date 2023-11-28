from Crypto.Util.number import *
import Crypto
import random
import libnum
    
def primitive_root(p_val: int) -> int:
    while True:
        g = random.randrange(3, p_val)
        if pow(g, 2, p_val) == 1:
            continue
        if pow(g, p_val, p_val) == 1:
            continue
        return g
    
bits = 1024

m = int(input("\nEnter integer message : "))
print("\nm = %d\n" % (m))

p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes) 

g = primitive_root(p)  
x1 = random.randrange(3, p)  
Y1 = pow(g,x1,p)
x2 = random.randrange(3, p)  
Y2 = pow(g,x2,p)
x3 = random.randrange(3, p)  
Y3 = pow(g,x3,p)

r1=random.randrange(3, p)  
r2=random.randrange(3, p)  
r3=random.randrange(3, p) 


print (f"\nPublic keys of participant : \n\ng = {g},  \n\np = {p}, \n\nY 1 = {Y1}, \n\nY 2 = {Y2}, \n\nY 3 = {Y3}")

print (f"\n\nPrivate keys of mix_server 1, mix_server 2 and mix_server 3 : \n\nx 1 = {x1}, \n\nr 1 = {r1}, \n\nx 2 = {x2}, \n\nr 2 = {r2}, \n\nx 3 = {x3}, \n\nr 3 = {r3}")


c11=pow(g,r1,p)
c21=(pow(Y1,r1,p)*m) % p

c12=pow(g,r2,p)
c22=(pow(Y2,r2,p)*c21) % p

c13=pow(g,r3,p)
c23=(pow(Y3,r3,p)*c22) % p


print (f"\n\nEncryption by participant : \n\nc 11 = {c11}\n\nc 21 = {c21}\n\n\nRe-encryption (2) by participant : \n\nc 12 = {c12}\n\nc 22 = {c22}\n\n\nRe-encryption (3) by participant : \n\nc 13 = {c13}\n\nc 23 = {c23}\n")


mix_server1_d = (c23*libnum.invmod(pow(c11,x1,p),p)) % p
print (f"\nDecryption by mix_server 1 : {mix_server1_d}" )
mix_server2_d = (mix_server1_d*libnum.invmod(pow(c12,x2,p),p)) % p
print (f"\nRe-decryption by mix_server 2 :  {mix_server2_d}" )
mix_server3_d =  (mix_server2_d*libnum.invmod(pow(c13,x3,p),p)) % p
print (f"\nRe-decryption by mix_server 3 :  {mix_server3_d}\n\n" )


