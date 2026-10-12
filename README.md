# Dice Roll Simulator

A simple desktop application developed using Python and Tkinter that allows users to simulate rolling multiple dice with a custom number of sides.

I built this project while completing the *VSCode for Developers: Set up a professional environment* guided course on Coursera. It gave me an opportunity to practise Python programming, work with graphical user interfaces, and become more familiar with using Visual Studio Code for software development.

## Features

- Roll multiple dice simultaneously.
- Choose the number of dice and sides.
- Generate random dice values using Python's `random` module.
- Display individual dice results and their combined total.
- Interact with the application through a Tkinter graphical interface.

## Technologies Used

- **Python 3** – Application logic and dice calculations
- **Tkinter** – Graphical user interface
- **Random module** – Random number generation
- **Visual Studio Code** – Development environment
- **Git & GitHub** – Version control and source code management

## How It Works

The application uses a function called `rollDie()` to generate a random integer between 1 and the number of sides specified.

When the user clicks the **Roll Dice** button, the program retrieves the values entered in the input fields and generates the requested number of dice rolls using a list comprehension.

The results are stored in a list, and the `sum()` function calculates their combined total. The Tkinter labels are then updated to display the individual values and total.

## Getting Started

### Prerequisites

- Python 3 installed
- Tkinter support available

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/ThiriWin-hub/dice-roll-simulator.git
```

**2. Navigate to the project directory**

```bash
cd dice-roll-simulator
```

**3. Run the application**

```bash
python roll_dice_simulator.py
```

On some systems, you may need to use `python3` instead.

The application will open in a separate desktop window.

## What I Learned

Working on this project helped me strengthen my understanding of Python fundamentals and how they can be applied to a working application.

I gained practical experience using functions, list comprehensions, random number generation, and Tkinter widgets. I also learned more about event-driven programming by connecting user interactions, such as clicking a button, to the application's functionality.

Alongside the programming itself, I practised using Git through the terminal to initialise a repository, commit changes and push my project to GitHub.

Although this is a small application, it has been a useful exercise in bringing together Python programming, GUI development, and basic version control in one project.
