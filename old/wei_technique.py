from Crypto.Util.number import *
import Crypto
import random


def find_primitive_element(p):
    if p == 2:
        return 1
    # the prime divisors of p-1 are 2 and (p-1)/2 because
    # p = 2x + 1 where x is a prime
    p1 = 2
    p2 = (p-1) // p1

    # test random g's until one is found that is a primitive root mod p
    while(1):
        g = random.randint(2, p-1)
        # g is a primitive root if for all prime factors of p-1, p[i]
        # g^((p-1)/p[i]) (mod p) is not congruent to 1
        if not (pow(g, (p-1)//p1, p) == 1):
            if not (pow(g, (p-1)//p2, p)) == 1:
                return g


def get_random_int(p):
    return random.randint(1, p-1)


def main():
    # input size in bits
    inputSize = 1000
    # Authorities for Multi Party Encryption
    authorities = 5

    # Generating Large Prime Number p
    p = getPrime(inputSize, randfunc=Crypto.Random.get_random_bytes)
    print("Generated Prime Number: ", p)

    # Calculating primitive element alpha
    alpha = find_primitive_element(p)
    print("\nPrimitive element: ", alpha)

    # Generating Keys
    a = [0] * authorities
    beta = [0] * authorities
    k = [0] * authorities

    for i in range(authorities):
        a[i] = get_random_int(p)
        beta[i] = pow(alpha, a[i], p)
        k[i] = get_random_int(p)

    # Message to be encrypted
    x = get_random_int(p)
    print("\nMessage to encrypt: ", x)

    # Encryption
    y1 = [0] * authorities
    y2 = [0] * authorities

    y1[0] = pow(alpha, k[0], p)
    y2[0] = (x*(pow(beta[0], k[0], p)) % p)
    print("\nEncrypted Messages: ")
    print("Ya [0]", "=", y1[0], "   ", "Yb [0]", "=", y2[0])

    # Re-Encryption
    for i in range(1, authorities):
        y1[i] = pow(alpha, k[i], p)
        y2[i] = (y2[i-1]*(pow(beta[i], k[i], p)) % p)
        print("Ya", [i], "=", y1[i], "   ", "Yb", [i], "=", y2[i])

    # Decryption
    d = y2[authorities-1]

    for i in range(1, authorities):
        d = (d * (pow(y1[i], p-1-a[i], p) % p)) % p

    # Re-Decryption
    t = (d * (pow(y1[0], p-1-a[0], p) % p)) % p

    print("\nDecrypted Message: ", t)


if __name__ == '__main__':
    main()
