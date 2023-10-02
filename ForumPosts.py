import random
diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []
while diamonds:
    user_input = input("Press enter to pick a card, or Q then enter to quit: ")
    if user_input == "Q":
        print("Goodbye!")
        break
    elif user_input == "":
        card = random.choice(diamonds)
        diamonds.remove(card)
        hand.append(card)
        print(f"Your Hand: {hand}")
        print(f"Remaining Cards: {diamonds}")
if not diamonds:
    print("There are no more cards to pick.")
