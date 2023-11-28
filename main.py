import os
import rsa_decryption_mixnet
import elgamal_decryption_mixnet
import visual_cryptography
import visual_cryptography_color


def clear_screen():
    try:
        # Check if running in an interactive terminal
        if os.isatty(0):
            os.system('cls' if os.name == 'nt' else 'clear')
    except AttributeError:
        # os.isatty is not available on all systems
        pass


def display_header():
    print("\033[95m=======================================================\033[0m")
    print("\033[95m    Khulna University of Engineering & Technology (KUET)    \033[0m")
    print("\033[95m      Dept. of Computer Science and Engineering          \033[0m")
    print("\033[95m    Programming Assignment on Advanced Cryptography    \033[0m")
    print("\033[95m        Submitted To: Dr. Md. Kazi Rokibul Alam          \033[0m")
    print("\033[95m=======================================================\033[0m")


def display_menu():
    print("\n                        Select your choice                        ")
    print(" [\033[92m1\033[0m] RSA Decryption Mixnet")
    print(" [\033[92m2\033[0m] Elgamal Decryption Mixnet")
    print(" [\033[92m3\033[0m] Visual Cryptography")
    print(" [\033[92m4\033[0m] Visual Cryptography (Color)")
    print(" [\033[91m0\033[0m] Exit")


def get_user_choice():
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None


def main():
    while True:
        clear_screen()
        display_header()
        display_menu()

        option = get_user_choice()

        if option is not None:
            if option == 1:
                rsa_decryption_mixnet.main()
            elif option == 2:
                elgamal_decryption_mixnet.main()
            elif option == 3:
                visual_cryptography.main()
            elif option == 4:
                visual_cryptography_color.main()
            elif option == 0:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
