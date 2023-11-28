from random import randrange
from Crypto.Util.number import getPrime
from Crypto.Random import get_random_bytes


def modular_inverse(a, m):
    """Calculate the modular inverse of a and m"""
    g, x, y = e_gcd(a, m)
    if g != 1:
        raise Exception('Modular Inverse Does Not Exist')
    else:
        x = x % m
        x = (x + m) % m
        return x


def multiplicative_inverse(a, m):
    """Calculate the multiplicative inverse of a and m"""
    g, x, y = e_gcd(a, m)
    if g != 1:
        raise Exception('Modular Inverse Does Not Exist')
    else:
        return x % m


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b"""
    while b:
        a, b = b, a % b
    return a


def e_gcd(a, b):
    """Calculate the Extended Euclidean Algorithm of a and b"""
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = e_gcd(b % a, a)
        return g, x - (b // a) * y, y


def random_prime_number(bits=1024) -> int:
    """
    Generate a random prime number using Crypto.Util.number.getPrime
    :param bits: number of bits
    :return: a random prime number
    """
    return getPrime(bits, randfunc=get_random_bytes)

# def random_prime_number(n: int) -> int:
#     """Generate a random prime number in range [2, n - 1]"""
#     prime_candidate = 1
#     while not check_prime(prime_candidate):
#         prime_candidate = randrange(2, n)
#     assert prime_candidate <= n
#     return prime_candidate
#
#
# def check_prime(n: int, k: int = 5) -> bool:
#     """Check if n is prime with Miller-Rabin primality test"""
#     if n < 2:
#         return False
#
#     if n == 2:
#         return True
#
#     if n % 2 == 0:
#         return False
#
#     # Write n as 2^s * d + 1
#     s, d = 0, n - 1
#     while d % 2 == 0:
#         s += 1
#         d //= 2
#
#     # Miller-Rabin primality test
#     def try_composite(a: int) -> bool:
#         x = pow(a, d, n)
#         if x == 1 or x == n - 1:
#             return False
#         for _ in range(s - 1):
#             x = pow(x, 2, n)
#             if x == n - 1:
#                 return False
#         return True
#
#     for _ in range(k):
#         a = randrange(2, n)
#         if try_composite(a):
#             return False
#
#     return True


# Example: get a random prime number in range [2**256, 2**200]
