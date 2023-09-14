# Monty Hall Problem Simulation

The Monty Hall problem is a probability puzzle rooted in a game show scenario. This repository provides a Python simulation to demonstrate the solution to the problem.

## Problem Description

Imagine you're a contestant on a game show. There are three doors in front of you:

1. Behind one door is a car.
2. Behind the other two doors are goats.

The game goes as follows:

1. You choose a door.
2. The host, Monty Hall, who knows what's behind each door, opens one of the other two doors to reveal a goat.
3. You then have a choice to stick with your original door or switch to the other unopened door.

The question is: Is it in your best interest to stick with your original choice, switch, or does it not matter?

## Solution

Statistically speaking, you have a better chance of winning the car if you always choose to switch. Your probability of winning if you stick with your original choice is 1/3, but if you switch, it becomes 2/3.

For an in-depth explanation, refer to the [Monty Hall problem on Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem).

## Python Simulation

The provided Python script simulates the Monty Hall problem multiple times to empirically demonstrate the above probabilities.

### How to Run

Ensure you have Python installed and then run the script:

```bash
python monty_hall_simulation.py


The script will simulate the game 1,000 times and provide statistics on the number of wins when sticking vs. switching.


