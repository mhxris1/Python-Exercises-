import random
print("Welcome to the Number Guessing Game")
guess_counter=0
guess_number= random.randint(1,1000)
game_run=True
print("The Number is between 1 and 1000")

while game_run==True:
    guess=int(input("Enter your guess: \n"))
    guess_counter += 1
    if guess<guess_number:
        print("Too Low. Try Again")
    elif guess>guess_number:
        print("Too High. Try Again")
    else:
        print(f"Well done. You guessed correctly in {guess_counter} guesses ")
        choice=input("Would You like to try again? (yes/no) : \n").lower()
        if choice == "yes":
            game_run=True
            guess_number= random.randint(1,1000)
            guess_counter=0
        else:
            game_run=False

print("Thanks for Playing. Goodbye!")
            




