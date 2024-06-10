import string
import random
characters = list(string.ascii_letters+string.digits+'!@#$%^&*()')


def genereatePassword():
    pass_length = int(input("enter the length of password:"))
    random.shuffle(characters)
    password = []
    for x in range(pass_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)
    print(password)


genereatePassword()
