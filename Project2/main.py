# Creating a Automated password genrator

import random
import string

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBERS = string.digits
CHAR = string.punctuation
ALL = UPPERCASE + LOWERCASE + NUMBERS + CHAR

while True:
    length = int(input("Length: "))
    password = "".join(random.sample(ALL, length))
    print(password)






