"""Russell Deady
Program to generate a random password
"""

import random

def main():

    #declaring variables
    amountOfLetters = 0
    password = ""
    shiftAmount = 0
    shift = []

    print()
    print("Welcome to the random password generator!")
    
    #letting user give the length of the password
    amountOfLetters = input("How many letters do you want the password to contain: ")
    print()

    #seeding random generator
    random.seed(a=None)
    
    #randomly generate the shift of each letter
    runs = 0
    while (runs < int(amountOfLetters)):
        shiftAmount = random.randint(0,25)
        shift.append(shiftAmount)
        runs += 1

    #generate the password by shifting each letter and adding it to the string
    runs = 0
    while (runs < int(amountOfLetters)):
        unicodeValue = 97
        unicodeValue = unicodeValue + shift[runs]
        newChar = chr(unicodeValue)
        password = password + newChar

        runs += 1

    print()
    print ("Your new password is",password) 
    print ("You should probably write that down somewhere!")
    print ("Thanks for using the random password generator!")
    print()


main()