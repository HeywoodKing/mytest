# Filename: while.py

number = 10
running = True

while running:
    guess = int(input("Enter a integer:"))

    if guess == number:
        print("Congratulations,you guessed it.")
        running = False
    elif guess < number:
        print("No,it is a little higher than that")
    else:
        print("No,it is a little lower than that")
# else:
print("The game is over.")
