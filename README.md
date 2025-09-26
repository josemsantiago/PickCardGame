# PickCardGame
### Simple Console Card Drawing Game

A basic Python card game where players draw cards from a deck of diamonds until all cards are drawn or they choose to quit.

## Overview

This simple console game simulates drawing cards from a standard deck of diamonds (13 cards). Players can repeatedly draw random cards, and the game continues until either all cards are drawn or the player chooses to quit.

## Features

- **13 Diamond Cards**: Uses a complete suit of diamonds (A, 2-10, J, Q, K)
- **Random Card Drawing**: Each card is randomly selected from remaining cards
- **Hand Tracking**: Displays current hand and remaining cards after each draw
- **Quit Option**: Players can exit anytime by pressing 'Q'
- **Game Completion**: Automatic end when all cards are drawn

## How to Play

1. Run the game: `python ForumPosts.py`
2. Press Enter to draw a random card
3. View your current hand and remaining cards
4. Continue drawing or press 'Q' + Enter to quit
5. Game ends when all 13 cards are drawn

## Technical Details

- **Language**: Python 3
- **Dependencies**: Only uses Python's built-in `random` module
- **Card Format**: Standard notation (AD = Ace of Diamonds, JD = Jack of Diamonds, etc.)
- **Deck Size**: 13 cards (one complete suit)

## Sample Gameplay

```
Press enter to pick a card, or Q then enter to quit:
Your Hand: ['7D']
Remaining Cards: ['AD', '2D', '3D', '4D', '5D', '6D', '8D', '9D', '10D', 'JD', 'QD', 'KD']

Press enter to pick a card, or Q then enter to quit:
Your Hand: ['7D', 'KD']
Remaining Cards: ['AD', '2D', '3D', '4D', '5D', '6D', '8D', '9D', '10D', 'JD', 'QD']

Press enter to pick a card, or Q then enter to quit: Q
Goodbye!
```

## Code Structure

```python
# Card deck initialization
diamonds = ["AD", "2D", "3D", ..., "KD"]  # 13 cards
hand = []  # Player's current hand

# Main game loop
while diamonds:  # Continue until deck is empty
    # Get user input (Enter or Q)
    # Draw random card and update hand
    # Display current state
```

## Game Rules

- Each card can only be drawn once (no duplicates)
- Cards are removed from the deck when drawn
- Player's hand grows with each card drawn
- Game automatically ends when deck is empty
- Player can quit voluntarily at any time

## Requirements

- Python 3.x
- No external dependencies required

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
