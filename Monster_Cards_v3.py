# Monster Cards V3 - 1/05/23
# Adds the add card function so users can add new cards to the deck

def print_deck():

    # Adding the deck display to a variable, so it can easily be printed
    deck_display = ""
    deck_display += "-------------------------\n"
    deck_display += "*** Full Card Deck ***\n"

    # Cycling and accessing values through the nested dictionary
    for monster_id, monster_info in deck.items():
        deck_display += f"\nMonster name: {monster_id}"
        for key in monster_info:
            deck_display += f"\n{key}: {monster_info[key]}"
        deck_display += "\n"

    deck_display += "-------------------------"
    print(deck_display)


def add_card():

    # Create new card name
    new_card = input("\nEnter the new monster name: ").upper()
    deck[new_card] = {}

    # Adds the values for 4 variables: strength, speed, stealth and cunning
    strength = int(input(f"\nEnter {new_card}'s strength value (1-25): "))
    deck[new_card]["Strength"] = strength
    speed = int(input(f"Enter {new_card}'s speed value (1-25): "))
    deck[new_card]["Speed"] = speed
    stealth = int(input(f"Enter {new_card}'s stealth value (1-25): "))
    deck[new_card]["Stealth"] = stealth
    cunning = int(input(f"Enter {new_card}'s cunning value (1-25): "))
    deck[new_card]["Cunning"] = cunning

    print(f"\nNew card {new_card} successfully added to the deck!")


def edit_card():
    print("edit card")


def del_card():
    print("delete card")


# Nested dictionary of all cards in the deck
deck = {
    "Stoneling":
        {"Strength": 7,
         "Speed": 1,
         "Stealth": 25,
         "Cunning": 15},
    "Vexscream":
        {"Strength": 1,
         "Speed": 6,
         "Stealth": 21,
         "Cunning": 19},
    "Dawnmirage":
        {"Strength": 5,
         "Speed": 15,
         "Stealth": 18,
         "Cunning": 22},
    "Blazegolem":
        {"Strength": 15,
         "Speed": 20,
         "Stealth": 23,
         "Cunning": 6},
    "Websnake":
        {"Strength": 7,
         "Speed": 15,
         "Stealth": 10,
         "Cunning": 5},
    "Moldvine":
        {"Strength": 21,
         "Speed": 18,
         "Stealth": 14,
         "Cunning": 5},
    "Vortexwing":
        {"Strength": 19,
         "Speed": 13,
         "Stealth": 19,
         "Cunning": 2},
    "Rotthing":
        {"Strength": 16,
         "Speed": 7,
         "Stealth": 4,
         "Cunning": 12},
    "Froststep":
        {"Strength": 14,
         "Speed": 14,
         "Stealth": 17,
         "Cunning": 4},
    "Wispghoul":
        {"Strength": 17,
         "Speed": 19,
         "Stealth": 3,
         "Cunning": 2}
}


# Main
print_deck()

choice = ""

# Main menu loop
while choice != "Z":
    choice = input("\n\nWhat would you like to do?"
                   "\nAdd new card (A)"
                   "\nEdit a card (E)"
                   "\nDelete a card (D)"
                   "\nPrint full deck (P)"
                   "\nExit (Z)"
                   "\n  >>> ").upper()

    if choice == "A":
        add_card()

    elif choice == "E":
        edit_card()

    elif choice == "D":
        del_card()

    elif choice == "P":
        print_deck()

    elif choice == "Z":
        print("\n*** Thank you for using this program ***")
