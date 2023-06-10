import random

def user_guess(number):
    random_number = random.randint(1,number)

    guess = 0
    while guess!=random_number:
        guess = int(input(f"Enter your guess between 1 and {number}: "))
        if guess<random_number:
            print("Guess is too low")

        elif guess>random_number:
            print("Guess is too high")

    print("congrats you're correct")

def computer_guess(number):
    high = number
    low = 1
    feedback = ""

    while feedback != "c":
        random_number = random.randint(low,high)
        print(random_number)
        feedback = input("Is guess too high(h), too low(l), or correct(c)?")
        if feedback == "h":
            high = random_number - 1
        if feedback == "l":
            low = random_number+1

    print("Correct number was guessed")

computer_guess(10)