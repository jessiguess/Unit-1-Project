print()
print("-" * 46)
print(" *** Welcome to the Number Guessing game! ***")
print("-" * 46)
print()


attempt_bank = [0]
import random
current_highscore = ("\n*** The current highscore is {} ***")
            
            
def guess_attempt():
    while True:
        try:
            guess = int(input("Please choose a number between 1 and 10:  "))
            if guess > 10:
                raise ValueError()
            elif guess < 1:
                raise ValueError()
        except ValueError:
            print("Sorry, only numbers between 1 and 10 are allowed in this game! Try again.")
        else:
            return guess

        
def start_game():
    answer = random.randint(1, 10)
    guess = 0
    attempts = 0
    while guess != answer:
        attempts += 1
        guess = guess_attempt()
        if guess > answer:
            print("That guess is too high! Try again.")
        elif guess < answer:
            print("That guess is too low! Try again.")
    print("{} was the correct answer! It took you {} tries to get it right.".format(answer, attempts))
    attempt_bank.append(attempts)
    
    
def high_score():
    for attempt in attempt_bank:
        if attempt_bank [0] == 0:
            print(current_highscore.format(attempt_bank [1]))
            del attempt_bank [0]
        elif attempt_bank [1] <= attempt_bank [0]:
            print(current_highscore.format(attempt_bank [1]))
            del attempt_bank [0]
        elif attempt_bank [1] > attempt_bank [0]:
            print(current_highscore.format(attempt_bank [0]))
            del attempt_bank [1]
    
    
def new_game():
    while True:
        new_game = input("Would you like to start a new game? Y/N:  ")
        
        if new_game.lower() == "y":
            high_score()
            start_game()
        else:
            print("Thank you for playing!")
            break
    
    
start_game()
new_game()

# Please reject my entry if it does not meet "Exceeds Expectations" criteria