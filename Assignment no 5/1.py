import random

def high_low_game():
    score = 0
    rounds = 3 

    print("Welcome to the Hassan's High-Low Game!")
    print(f"You will play {rounds} rounds against the computer.")
    
    for round_number in range(1, rounds + 1):
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"\nRound {round_number}:")
        print(f"Your number is: {player_number}")
        
        guess = input("Do you think your number is 'higher' or 'lower' than the computer's number? ").lower()
        
        if (guess == 'higher' and player_number > computer_number) or \
           (guess == 'lower' and player_number < computer_number):
            print("Correct! You get a point.")
            score += 1
        else:
            print("Wrong guess. No point for this round.")
        
        print(f"The computer's number was: {computer_number}")

    print("\nGame over!")
    print(f"Your final score is: {score} out of {rounds}")

high_low_game()
