from random import randint
import helpers

number_of_mix_server = 3  # default number of mix server


def generate_private_key(p):
    """Generate a private key in range [10^20, p - 1]"""
    key = randint(10 ** 20, p)
    while helpers.gcd(p, key) != 1:
        key = randint(10 ** 20, p)
    return key


def main():
    global number_of_mix_server
    i = input("enter the number of mixnet-router (default:3) : ")
    if i != '':
        number_of_mix_server = int(i)

    # a large prime number, p
    p = helpers.random_prime_number()
    # a random integer, g
    g = randint(2, p)
    mix_server_private_key = []
    Y = 1
    for i in range(number_of_mix_server):
        print("\033[95m--------- Key Gen for Mix Server : ", i + 1, " ------------\033[0m")
        private_key = generate_private_key(p)
        mix_server_private_key.append(private_key)
        bita = pow(g, private_key, p)
        Y = (Y * bita) % p
        print("Private key is: ", private_key)
        print("Public key is: ", Y)
        print("-----------------------------------------------------------------------")

    msg = int(input("What is your message: "))
    print("\033[95m--------- Encrypting the message ------------\033[0m")
    r = randint(2, 10 ** 40)
    print("r: ", r)
    # c1 = g^r mod p
    c1 = pow(g, r, p)
    print("c1 : ", c1)
    # c2 = (msg * Y^r) mod p
    print("c2: ", Y)
    c2 = ((msg % p) * pow(Y, r, p)) % p

    print("----------------------------------------")
    print("\033[92mEncrypted Message: " + str(c2) + "\033[0m")
    print("----------------------------------------")

    i = input("Do you want to decrypt the message? (y/n): ")
    if i == 'y':
        print("Decrypting the message...")
        for i in range(number_of_mix_server):
            print("\033[95m--------- Decryption from Mix Server : ", i + 1, " ------------\033[0m")
            # temp = c1^private_key mod p
            temp = pow(c1, mix_server_private_key[i], p)
            inv = helpers.modular_inverse(temp, p)
            # c2 = (c2 * Y^(-r)) mod p
            c2 = (c2 * inv) % p
            print("c1 : ", c1)
            print("c2 : ", c2)
            print("-----------------------------------------------------------------------")

        print("----------------------------------------")
        print("\033[92mFinal Plain Message: " + str(c2) + "\033[0m")
        print("----------------------------------------")
    else:
        print("Exiting...")


if __name__ == '__main__':
    main()
