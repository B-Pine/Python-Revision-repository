import string
import time
import random


def password_generator(length: int = 8) -> str:
    characters = list(string.ascii_letters + string.digits + "!#$%&*(){}:")
    password_container = []
    for char in range(length):
        random.shuffle(characters)
        password_container.append(characters[0])
    return "".join(password_container)


is_continue = True
while is_continue:
    print("Generate password? (y/n) ")
    is_continue = input(">> ")
    if is_continue not in ["y", "n"]:
        print("Enter valid choice!")
        break
    is_continue = True if is_continue == 'y' else False

    if is_continue:
        password_length = int(input("Password length: "))
        print("\tGenerating password..")
        password = password_generator(password_length)
        time.sleep(0.5)
        print(f"\tGenerated password: {password}")
    else:
        print('Thank you! See you!')
        break
