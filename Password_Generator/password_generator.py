import random
import string

while True:
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    print("Generated Password:", password)

    again = input("Do you want to generate another password? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using the Password Generator!")
        break