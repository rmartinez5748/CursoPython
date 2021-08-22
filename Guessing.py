number = 9
trial = 1

while trial <= 3:
    guess = int(input("What is the number that you guess: "))
    if guess == number:
        print("Congratulations you guessed the number")

    else:
        trial = trial+1

if trial > 3:
    print("You missed the chance to guess the number")
