from random import randint

number = randint(0, 20)
guess = -1

while guess != number:
    while True:
        try:
            guess = int(input("Enter number between 0 and 20: "))
        except ValueError:
            print ("Not a number")
        
        if guess > 0 and guess < 21:
            break
        else:
            print("Should be between 0 and 20")
            continue

    if guess > number:
        print("Your number is too high")
    elif guess < number:
        print("Your number is too low")
    else:
        print("Your number is just right")
        break
