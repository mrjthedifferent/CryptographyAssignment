import helpers

number_of_mix_server = 3  # default number of mix server


def generate_keys():
    """
    Generate public, private and random key
    :return: public key, private key and random key
    Generation Rules:
    1. p and q are two large primes
    2. n = p * q
    3. phi = (p - 1) * (q - 1)
    4. e is relatively prime to phi and 1 < e < phi
    5. d is the multiplicative inverse of e mod phi
    6. public key is (e, n)
    7. private key is (d, n)
    """
    p = helpers.random_prime_number()
    q = helpers.random_prime_number()
    r = helpers.random_prime_number()
    print('p: ', p)
    print('q: ', q)
    print('r: ', r)
    n = p * q
    print('n: ', n)
    phi = (p - 1) * (q - 1)
    e = 3
    g = helpers.gcd(e, phi)
    while g != 1:
        e = e + 1
        g = helpers.gcd(e, phi)
    d = helpers.multiplicative_inverse(e, phi)
    print('e: ', e)
    print('d: ', d)
    print('phi: ', phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key, r


def encryption(m, pub_key, pri_key, r):
    """
    Encrypt the message using public key
    :param m: message
    :param pub_key: Public key
    :param pri_key: Private key
    :param r: random string
    :return: ciphertext
    """
    for i in range(number_of_mix_server):
        print("\033[95m---------- Encryption for Mix Server : ", i + 1, " ------------\033[0m")
        e, n = pub_key[i]
        d, n = pri_key[i]
        R = r[i]
        print("Message (m) : ", m)
        print("e : ", e)
        print("d : ", d)
        print("r : ", R)
        print("n : ", n)
        m = m + R
        ciphertext = pow(m, e, n)
        print("Encrypted data : ", ciphertext)
        m = ciphertext
        print("-----------------------------------------------------------------------")

    print("----------------------------------------")
    print("\033[92mFinal Cipher text : ", ciphertext, "\033[0m")
    print("----------------------------------------")
    return ciphertext


def decryption(ciphertext, pub_key, pri_key, r):
    """
    Decrypt the message using private key
    :param ciphertext: Cipher text
    :param pub_key: Public key
    :param pri_key: Private key
    :param r: random string
    """
    repr(ciphertext)
    b = input("Do you want to decrypt the message? (y/n): ")
    if b == 'y':
        j = -1
        i = 0
        plaintext = 0
        while j > -(number_of_mix_server + 1):
            print("\033[95m---------- Decryption for Mix Server : ", i + 1, " ------------\033[0m")
            e, n = pub_key[j]
            d, n = pri_key[j]
            R = r[j]
            print("m : ", ciphertext)
            print("e : ", e)
            print("d : ", d)
            print("r : ", R)
            print("n : ", n)
            plaintext = pow(ciphertext, d, n)
            plaintext = int(plaintext - R)
            print('Decryption: ', plaintext)
            ciphertext = plaintext
            j = j - 1
            i = i + 1
            print("-----------------------------------------------------------------------")

        print("----------------------------------------")
        print("\033[92mFinal Plaintext : ", plaintext, "\033[0m")
        print("----------------------------------------")
    else:
        print(" Exiting the program. Goodbye! ")


def main():
    global number_of_mix_server
    pub_key = []
    pri_key = []
    random_string = []

    i = input("Enter the number of mixnet-router (default:3) : ")
    if i != '':
        number_of_mix_server = int(i)

    for i in range(number_of_mix_server):
        print("\033[95m--------- Private & Public Key Gen for Mix Server : ", i + 1, " ------------\033[0m")
        public_key, private_key, r = generate_keys()
        pub_key.append(public_key)
        pri_key.append(private_key)
        random_string.append(r)
        print("Public key is: ", public_key)
        print("Private key is: ", private_key)
        print("-----------------------------------------------------------------------")

    print("-------------------------------------------------")
    m = int(input('Enter Message, M: '))
    print("-------------------------------------------------")
    ciphertext = encryption(m, pub_key, pri_key, random_string)
    decryption(ciphertext, pub_key, pri_key, random_string)


if __name__ == '__main__':
    main()
