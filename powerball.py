import random
import json

white_possibles = list(range(1, 70))
red_possibles = list(range(1, 27))

tickets_per_drawing = 250000
num_drawings = 156
0
total_spent = 0
earnings = 0

times_won = {
    "5+P": 0,
    "5": 0,
    "4+P": 0,
    "4": 0,
    "3+P": 0,
    "3": 0,
    "2+P": 0,
    "1+P": 0,
    "P": 0,
    "0": 0
}


def calc_win_amt(my_numbers, winning_numbers):
    """
    Calculate the amount won based on the numbers played and the winning numbers for a drawing.
    """
    win_amt = 0

    white_matches = len(my_numbers["whites"].intersection(
        winning_numbers["whites"]))
    power_match = my_numbers["red"] == winning_numbers["red"]

    if white_matches == 5 and power_match:
        win_amt = 1000000000
        times_won["5+P"] += 1
    elif white_matches == 5:
        win_amt = 1000000
        times_won["5"] += 1
    elif white_matches == 4 and power_match:
        win_amt = 50000
        times_won["4+P"] += 1
    elif white_matches == 4:
        win_amt = 100
        times_won["4"] += 1
    elif white_matches == 3 and power_match:
        win_amt = 100
        times_won["3+P"] += 1
    elif white_matches == 3:
        win_amt = 7
        times_won["3"] += 1
    elif white_matches == 2 and power_match:
        win_amt = 7
        times_won["2+P"] += 1
    elif power_match:
        win_amt = 4
        times_won["P"] += 1
    elif white_matches == 1 and power_match:
        win_amt = 4
        times_won["1+P"] += 1
    else:
        times_won["0"] += 1

    return win_amt


for drawing in range(num_drawings):
    white_drawing = set(random.sample(white_possibles, k=5))  # 5 white balls
    red_drawing = random.choice(red_possibles)  # 1 red ball

    winning_numbers = {"whites": white_drawing, "red": red_drawing}

    for ticket in range(tickets_per_drawing):  # Buy tickets for this drawing
        total_spent += 2  # $2 per ticket
        my_white = set(random.sample(white_possibles, k=5))
        my_red = random.choice(red_possibles)

        my_numbers = {
            "whites": my_white,
            "red": my_red
        }

        # Calculate winnings
        win_amt = calc_win_amt(my_numbers, winning_numbers)
        earnings += win_amt  # Add winnings to total earnings

print(f"Total spent: ${total_spent}")
print(f"Total earnings: ${earnings}")
print(f"Net profit: ${earnings - total_spent}")

print(json.dumps(times_won, indent=4))
