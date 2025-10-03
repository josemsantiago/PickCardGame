# PickCardGame
### Simple Console Card Drawing Game

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-active-success)

A basic Python card game where players draw cards from a deck of diamonds until all cards are drawn or they choose to quit.

## Screenshots

> **Note:** Console output screenshots will be added soon. Run `python pick_card_game.py` to see the game in action.

## Overview

This simple console game simulates drawing cards from a standard deck of diamonds (13 cards). Players can repeatedly draw random cards, and the game continues until either all cards are drawn or the player chooses to quit.

## Features

- **13 Diamond Cards**: Uses a complete suit of diamonds (A, 2-10, J, Q, K)
- **Random Card Drawing**: Each card is randomly selected from remaining cards
- **Hand Tracking**: Displays current hand and remaining cards after each draw
- **Quit Option**: Players can exit anytime by pressing 'Q'
- **Game Completion**: Automatic end when all cards are drawn

## How to Play

1. Run the game: `python pick_card_game.py`
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

## Prerequisites

- **Python**: version 3.6 or higher ([Download](https://www.python.org/downloads/))
- **No external dependencies required** - uses only Python's built-in `random` module

To check your Python version:
```bash
python --version
# or
python3 --version
```

## Troubleshooting

### Common Issues

**Issue:** `python: command not found`

**Solution:** Install Python 3 from [python.org](https://www.python.org/downloads/) or use `python3 pick_card_game.py` instead.

---

**Issue:** Game doesn't recognize 'Q' to quit

**Solution:** Ensure you're pressing 'Q' followed by Enter. The input is case-sensitive (use uppercase Q).

---

**Issue:** Cards appear to repeat

**Solution:** The game removes cards from the deck after drawing. If you see duplicates, please report this as a bug.

---

**Issue:** Script exits with "list index out of range"

**Solution:** This shouldn't happen in normal gameplay. If it does, please report the bug with steps to reproduce.

For additional help, please open an issue in the repository issue tracker.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

### Enhancement Ideas
- Add multiple suits (hearts, clubs, spades)
- Implement card game rules (e.g., poker hands)
- Add scoring system
- Create ASCII art for cards
- Build a GUI version

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact & Support

- **Author**: Jose Santiago Echevarria
- **Issues**: Please report bugs via the repository issue tracker
- **Educational Purpose**: This project demonstrates Python lists, loops, random selection, and user input handling
