import wei_technique
import visual_cryptography


def menu():
    print("\033c")
    print()
    print("=======================================================")
    print("    Khulna University of Engineering & Technology (KUET)    ")
    print("      Dept. of Computer Science and Engineering          ")
    print(" Programming Assignment on Principles of Cryptography")
    print("           Submitted To: Dr. Md. Kazi Rokibul Alam          ")
    print()
    print()
    print("                        Select your choice                        ")
    print(" [1] Wei's Technique")
    print(" [2] Hwang's Blind Signature")
    print(" [3] Visual Cryptography")
    print(" [0] Exit")
    print("========================================================")


menu()
option = int(input("Enter your choice: "))

while option != 0:
    if option == 1:
        option = 0
        wei_technique.main()
    if option == 2:
        option = 0
        print("Not Completed Yet")
    if option == 3:
        option = 0
        visual_cryptography.main()
