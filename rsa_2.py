from Crypto.Util.number import getPrime, getRandomRange
import libnum
import math

def generate_key_pair(bits, PHI, n):
    e = getRandomRange(2, PHI)
    while math.gcd(e, PHI) != 1:
        e = getRandomRange(2, PHI)

    d = libnum.invmod(e, PHI)
    while (e * d) % PHI != 1:
        d = getRandomRange(2, n)

    return e, d

def generate_key_pair_with_phi(bits, PHI, n):
    e = getRandomRange(2, PHI)
    while math.gcd(e, PHI) != 1:
        e = getRandomRange(2, PHI)

    d = libnum.invmod(e, PHI)
    while (e * d) % PHI != 1:
        d = getRandomRange(2, PHI)

    return e, d

def encrypt_decrypt(msg, e, d, n):
    c = pow(msg, e, n)
    decrypted_msg = pow(c, d, n)
    return c, decrypted_msg

bits = 1024

msg = int(input("\nEnter concatenated integer message: "))

p = getPrime(bits)
q = getPrime(bits)
n = p * q
PHI = (p - 1) * (q - 1)

e_p1, d_p1 = generate_key_pair(bits, PHI, n)
e_p2, d_p2 = generate_key_pair(bits, PHI, n)
e_p3, d_p3 = generate_key_pair(bits, PHI, n)

c1, d1 = encrypt_decrypt(msg, e_p1, d_p1, n)
c2, d2 = encrypt_decrypt(c1, e_p2, d_p2, n)
c3, d3 = encrypt_decrypt(c2, e_p3, d_p3, n)

print("\n\nConcatenated integer message of participant =", msg)
print("Encryption by participant =", c1)
print("Re-encryption (2) by participant =", c2)
print("Re-encryption (3) by participant =", c3)
print("Decryption by mix_server 1 =", d1)
print("Re-decryption by mix_server 2 =", d2)
print("Re-decryption by mix_server 3 =", d3)

msg2 = int(input("\nEnter private integer message: "))

p2 = getPrime(bits)
q2 = getPrime(bits)
n2 = p2 * q2
PHI2 = (p2 - 1) * (q2 - 1)

e_p4, d_p4 = generate_key_pair_with_phi(bits, PHI2, n2)
e_p5, d_p5 = generate_key_pair_with_phi(bits, PHI2, n2)
e_p6, d_p6 = generate_key_pair_with_phi(bits, PHI2, n2)

c4, d4 = encrypt_decrypt(msg2, e_p4, d_p4, n2)
c5, d5 = encrypt_decrypt(c4, e_p5, d_p5, n2)
c6, d6 = encrypt_decrypt(c5, e_p6, d_p6, n2)

print("\n\nPrivate integer message of participant =", msg2)
print("Encryption by participant =", c4)
print("Re-encryption (2) by participant =", c5)
print("Re-encryption (3) by participant =", c6)
print("Decryption by mix_server 1 =", d4)
print("Re-decryption by mix_server 2 =", d5)
print("Re-decryption by mix_server 3 =", d6)

ms = msg - msg2
print("\nActual message (concatenated-private) =", ms)
