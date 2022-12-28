import random


def is_guessed_number_correct(realNumber, guessedNumber):
    if (realNumber == guessedNumber):
        return True
    else:
        return False

def hint_user(realNumber, guessedNumber):
        if(realNumber<guessedNumber):
            print("try a smaller number")
        else:
            print("try a bigger number")
number = random.randint(0, 10)
count = 0
while count <= 5:
    print("Guess a Numebr", number)
    guessedNumber = int(input())

    if is_guessed_number_correct(number, guessedNumber):
        print('congradulation!')
        break
    else:
        hint_user(number, guessedNumber)
        count = count + 1
    if count==5:
        print("you lost the number is :", number)