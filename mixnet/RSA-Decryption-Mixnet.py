from Crypto.Util.number import *
import Crypto
import libnum
import math

bits = 1024

print("\n- 1st part -\n")

msg = int(input("\nEnter concatenated integer message : "))

p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes) #This line generates a random prime number with a specified number of bits using the getPrime function from the Crypto.Util.number module. The randfunc parameter is set to use random bytes from Crypto.Random.get_random_bytes for randomness.
q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
n = p * q
PHI = (p - 1) * (q - 1)

print("\n\np 1 = %s\n\nq 1 = %s\n\nn 1 = %s\n\nphi 1 = %s\n" % (p, q, n, PHI))


def generate_key_pair(bits, PHI, n):
    while True:
        e = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
        if 1 < e < PHI and math.gcd(e, PHI) == 1:
            break

    while True:
        d = libnum.invmod(e, PHI)
        if (e * d) % PHI == 1 and 0 <= d <= n:
            break

    return e, d

e_p1, d_p1 = generate_key_pair(bits, PHI, n)
e_p2, d_p2 = generate_key_pair(bits, PHI, n)
e_p3, d_p3 = generate_key_pair(bits, PHI, n)

print("\n\nParticipant's keys : \n\ne 1 = %d, \n\nd 1 = %d\n\ne 2 = %d, \n\nd 2 = %d\n\ne 3 = %d, \n\nd 3 = %d" % (e_p1, d_p1, e_p2, d_p2, e_p3, d_p3))

c1 = pow(msg, e_p1, n)
c2 = pow(c1, e_p2, n)
c3 = pow(c2, e_p3, n)

d1 = pow(c3, d_p1, n)
d2 = pow(d1, d_p2, n)
d3 = pow(d2, d_p3, n)

print("\n\n\nConcatenated integer message of participant = %s\n\nEncryption by participant = %s\n\nRe-encryption (2) by participant = %s\n\nRe-encryption (3) by participant = %s\n\nDecryption by mix_server 1 = %s\n\nRe-decryption by mix_server 2 = %s\n\nRe-decryption by mix_server 3 = %s\n\n" % (msg, c1, c2, c3, d1, d2, d3))


print("\n\n- 2nd part -\n")

msg2 = int(input("\nEnter private integer message: "))

p2 = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
q2 = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
n2 = p2 * q2
PHI2 = (p2 - 1) * (q2 - 1)

print("\np 2 = %s\n\nq 2 = %s\n\nn 2 = %s\n\nphi 2 = %s\n" % (p2, q2, n2, PHI2))

def generate_key_pair_with_phi(bits, PHI2, n2):
    while True:
        e = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
        if e < PHI2 and math.gcd(e, PHI2) == 1:
            break

    while True:
        d = libnum.invmod(e, PHI2)
        if d < PHI2 and (e * d) % PHI2 == 1:
            break

    return e, d


e_p4, d_p4 = generate_key_pair_with_phi(bits, PHI2, n2)
e_p5, d_p5 = generate_key_pair_with_phi(bits, PHI2, n2)
e_p6, d_p6 = generate_key_pair_with_phi(bits, PHI2, n2)

print("\n\nParticipant's keys : \n\ne 1 = %d, \n\nd 1 = %d\n\ne 2 = %d, \n\nd 2 = %d\n\ne 3 = %d, \n\nd 3 = %d" % (e_p4, d_p4, e_p5, d_p5, e_p6, d_p6))

c4 = pow(msg2, e_p4, n2)
c5 = pow(c4, e_p5, n2)
c6 = pow(c5, e_p6, n2)

d4 = pow(c6, d_p4, n2)
d5 = pow(d4, d_p5, n2)
d6 = pow(d5, d_p6, n2)

print("\n\n\nPrivate integer message of participant = %s\n\nEncryption by participant = %s\n\nRe-encryption (2) by participant = %s\n\nRe-encryption (3) by participant = %s\n\nDecryption by mix_server 1 = %s\n\nRe-decryption by mix_server 2 = %s\n\nRe-decryption by mix_server 3 = %s\n\n" % (msg2, c4, c5, c6, d4, d5, d6))


ms = msg - msg2

print("\n\nActual message (concatenated-private) = %d\n\n\n" % (ms))

