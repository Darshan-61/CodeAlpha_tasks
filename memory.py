import random

# Create a list of words to use as card faces
words = ["apple", "banana", "cherry", "date"]

# Create a list to store the cards
cards = []

# Create pairs of cards with the same word
for word in words:
    cards.append({"word": word, "flipped": False})
    cards.append({"word": word, "flipped": False})

# Shuffle the cards
random.shuffle(cards)

# Print the cards
for i, card in enumerate(cards):
    print(f"Card {i+1}: {'?' if not card['flipped'] else card['word']}")

# Game loop
while True:
    # Ask the user to choose two cards
    card1_index = int(input("Enter the number of the first card: ")) - 1
    card2_index = int(input("Enter the number of the second card: ")) - 1

    # Flip the cards
    cards[card1_index]["flipped"] = True
    cards[card2_index]["flipped"] = True

    # Print the cards
    for i, card in enumerate(cards):
        print(f"Card {i+1}: {'?' if not card['flipped'] else card['word']}")

    # Check if the cards match
    if cards[card1_index]["word"] == cards[card2_index]["word"]:
        print("Match found!")
    else:
        print("No match found.")
        # Flip the cards back
        cards[card1_index]["flipped"] = False
        cards[card2_index]["flipped"] = False

    # Check if all cards have been matched
    if all(card["flipped"] for card in cards):
        print("Congratulations, you won!")
        break