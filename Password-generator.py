import string
import random

random_string = '' # Start with an empty string
count = 0 # this will keep track of how many characters to have in password

while count < 12:
    random_string += random.choice(string.ascii_lowercase) #keep choosing random letter
    count += 1 

    print(random_string)
