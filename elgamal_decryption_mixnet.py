from random import randint
import helpers

number_of_mix_server = 2  # default number of mix server


def generate_private_key(p):
    """Generate a private key in range [10^20, p - 1]"""
    key = randint(10 ** 20, p)
    while helpers.gcd(p, key) != 1:
        key = randint(10 ** 20, p)
    return key


def main():
    global number_of_mix_server
    i = input("enter the number of mixnet-router (default:2) : ")
    if i != '':
        number_of_mix_server = int(i)

    p = helpers.random_prime_number()
    alpha = randint(2, p)
    mix_server_private_key = []
    mix_server_bita_key = []
    Y = 1
    for i in range(number_of_mix_server):
        print("--------- Key Gen for Mix Server : ", i + 1, " ------------")
        private_key = generate_private_key(p)
        mix_server_private_key.append(private_key)
        bita = pow(alpha, private_key, p)
        mix_server_bita_key.append(bita)
        Y = (Y * bita) % p
        print("Private key is: ", private_key)
        print("Public key is: ", bita)
        print("-----------------------------------------------------------------------")

    r = randint(2, 10 ** 40)
    c1 = pow(alpha, r, p)
    msg = int(input("What is your message: "))
    c2 = ((msg % p) * pow(Y, r, p)) % p

    print("----------------------------------------")
    print("Encrypted Message: " + str(c2))
    print("----------------------------------------")

    i = input("Do you want to decrypt the message? (y/n): ")
    if i == 'y':
        print("Decrypting the message...")
        for i in range(number_of_mix_server):
            print("--------- Decryption from Mix Server : ", i + 1, " ------------")
            temp = pow(c1, mix_server_private_key[i], p)
            inv = helpers.modular_inverse(temp, p)
            c2 = (c2 * inv) % p
            print("c1 : ", c1)
            print("c2 : ", c2)
            print("-----------------------------------------------------------------------")

        print("----------------------------------------")
        print("Final Plain Message: " + str(c2))
        print("----------------------------------------")
    else:
        print("Exiting...")

if __name__ == '__main__':
    main()
