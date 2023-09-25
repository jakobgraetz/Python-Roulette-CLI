import random

if __name__ == '__main__':
    try:
        with open("win.txt", "r") as file:
            win = int(file.readline())
    except FileNotFoundError:
        win = 0
    try:
        with open("loss.txt", "r") as file:
            loss = int(file.readline())
    except FileNotFoundError:
        loss = 0
    try:
        with open("roulette.txt", "r") as file:
            cash = int(file.readline())
    except FileNotFoundError:
        cash = 100
    print(f"Welcome to your favorite casino, Grätz CASINO! Your balance is {cash}")
    while True:
        bet = input("How much do you want to bet?")
        if bet.isdigit() and 0 < int(bet) <= cash:
            print(f"You're betting {bet}!")
            break
        else:
            print("Invalid Input!")
    while True:
        command = input("let the ball roll> ").lower().strip()
        if command in ['quit', 'leave', 'exit', 'stop']:
            break
        elif command == "red":
            guess = [number for number in range(1, 36, 2)]
        elif command == "black":
            guess = [number for number in range(2, 38, 2)]
        else:
            try:
                guess = [int(command)]
            except ValueError:
                print("your input was malformed; please enter a number between 0 and 36;")
                print("you may also choose 'red' or 'black' or enter 'quit', 'exit', or 'leave'")
                continue
        print(f"you guessed: {guess}")
        print("Rien ne va plus")
        number = random.randint(0, 37)
        print(f"The number was {number}")
        if number in guess and int(bet) > 0:
            winner_message = random.choice(["Winner, winner, chicken dinner!", "Yeeeeehaaw!", "cool"])
            print(winner_message)
            win_value = int(bet)*36/len(guess)
            win_value = int(win_value)
            print(f"You won {win_value}")
            cash = cash + win_value
            print(f"Your new balance is {cash}")
            win = win + 1
        else:
            loser_message = random.choice(["F***!", "LOOOOOOSER!", "Better try harder next time!"])
            print(loser_message)
            print(f"You lost {bet}")
            bet_value = int(bet)
            cash = cash - bet_value
            print(f"Your new balance is {cash}")
            loss = loss + 1
    with open("roulette.txt", "w") as file:
        file.write(f"{cash}")
    with open("loss.txt", "w") as file:
        file.write(f"{loss}")
    with open("win.txt", "w") as file:
        file.write(f"{win}")
