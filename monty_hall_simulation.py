import random


def monty_hall_simulation(num_trials=1000):
    stick_wins = 0
    switch_wins = 0

    for _ in range(num_trials):
        # Place car behind one door
        car_position = random.randint(1, 3)

        # Contestant makes an initial choice
        contestant_choice = random.randint(1, 3)

        # Monty opens one of the doors with a goat
        remaining_doors = [door for door in [1,2,3] if door != contestant_choice and door != car_position]
        monty_opens = random.choice(remaining_doors)

        # Determine the door if the contestant switches
        switch_choice = [door for door in [1,2,3] if door != contestant_choice and door != monty_opens][0]

        # Update win counters
        if contestant_choice == car_position:
            stick_wins += 1
        if switch_choice == car_position:
            switch_wins += 1

    print(f"Stick Wins: {stick_wins/num_trials:.2%}")
    print(f"Switch Wins: {switch_wins/num_trials:.2%}")


if __name__ == "__main__":
    monty_hall_simulation()
