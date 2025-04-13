import random

NUM_SIDES = 6

def roll_dice() -> tuple[int, int, int]:
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    return die1, die2, total
