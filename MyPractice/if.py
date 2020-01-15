# Filename: if.py

number = 10
guess = int(input("Enter a integer:"))

if guess == number:
    print("Congratulations,you guessed it.")
elif guess < number:
    print("No,it is a little highter than that")
else:
    print("No,it is a little lower than that")

a = 100
if a >= 0:
	print(a)
else:
	print(-a)
