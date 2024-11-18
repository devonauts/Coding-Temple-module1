import random

guessedNumber = 0

if guessedNumber == 0 :
    guessedNumber = int(input("Guess a number from 1 - 10?"),0)
    if guessedNumber is 0 or guessedNumber > 10 :
        print("incorrect field, please choose a number between 1 and 10")
        guessedNumber = 0
        guessedNumber = int(input("Guess a number from 1 - 10?"),0)
    else:
        random_number = random.randrange(1,10)
        if random_number == guessedNumber :
            print("Congratulations!, you guessed the number")
        if guessedNumber < random_number :
            print("Too low")
        else: 
            print("TOO HIGH")

else:
    print("all good")
