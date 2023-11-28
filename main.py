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
    print("=======================================================")
    print("    Khulna University of Engineering & Technology (KUET)    ")
    print("      Dept. of Computer Science and Engineering          ")
    print("    Programming Assignment on Advanced Cryptography    ")
    print("           Submitted To: Dr. Md. Kazi Rokibul Alam          ")
    print("=======================================================")


def display_menu():
    print("\n                        Select your choice                        ")
    print(" [1] RSA Decryption Mixnet")
    print(" [2] Elgamal Decryption Mixnet")
    print(" [3] Visual Cryptography")
    print(" [4] Visual Cryptography (Color)")
    print(" [0] Exit")


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
