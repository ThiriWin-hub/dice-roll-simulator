# roll_dice_simulator.py

import random
import tkinter as tk

def roll_die(sides)=6):
    return random.randint(1, SIDES)


def roll_multiple_dice(numDice, sides):
    """
    Simulates rollling multiple dice of the same number of sides.

    Args:
        numDice (int): The number of dice to roll.
        sides (int): The number of sides on each die.

    Returns:
        tuple: A tuple containing two elements:
            - A list of integers representing the result of each dice roll.
            - An integer representing the sum of all dice rolls.
    """
    results = [roll_dice(sides) for _ in range(numDice)]
    return results, sum(results)

def roll_dice():
    num_dice = int(num_dice_entry.get())
    sides = int(sides_Entry.get())
    results, total = roll_multiple_dice(num_dice, sides)
    results_label.config(text=f"You rolled: {results}")
    total_label.config(text=f"Total: {total}")

def initialize_gui_app():
    root = tk.Tk()
    root.title("Dice Roll Simulator")
    return root


def create_labels(root):
    tk.Label(root, text="Number of Dice:").grid(row=0, column=0)
    tk.Label(root, text="Number of Sides:").grid(row=1, column=0)
    results_label = tk.Label(root, text="You rolled: ")
    total_label= tk.Label(root, text="Total: ")
    return results_label, total_label


def create_widgets(roll_dice, root):
    num_dice_entry = tk.Entry(root)
    sides_entry = tk.Entry(root)
    roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
    return num_dice_entry, sides_entry, roll_button


def set_grid(results_label, total_label, num_dice_entry, sides_entry, roll_button)
    num_dice_entry.grid(row=0, column=1)
    sides_entry.grid(row=1, column=1)
    roll_button.grid(row=2, column=0, columnspan=2)
    results_lablel.grid(row=3, column=0, columnspan=2)
    total_label.grid(row=4, column=0, columnspan=2)


root = initialize_gui_app()
results_label, total_label = create_labels(root)
num_dice_entry, sides_entry, roll_button = create_widgets(roll_dice, root)
set grid(results_label, total_label, num_dice_entry, sides_entry, roll_button)
root.mainloop()