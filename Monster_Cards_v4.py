# Monster Cards V3 - 2/05/23
# Adds the edit card function so the user can edit values for existing cards

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


# Add new card
def add_card():

    # Create new card name
    new_card = input("\nEnter the new monster name: ").title()
    deck[new_card] = {}

    # Adds the values for 4 variables: strength, speed, stealth and cunning between 1 and 25
    strength = int(input(f"\nEnter {new_card}'s strength value (1-25): "))
    if 1 < strength < 25:
        deck[new_card]["Strength"] = strength
    else:
        print("Value not accepted (Please add Strength using the edit function)")

    speed = int(input(f"\nEnter {new_card}'s speed value (1-25): "))
    if 1 < speed < 25:
        deck[new_card]["Speed"] = speed
    else:
        print("Value not accepted (Please add Speed using the edit function)")

    stealth = int(input(f"\nEnter {new_card}'s stealth value (1-25): "))
    if 1 < stealth < 25:
        deck[new_card]["Stealth"] = stealth
    else:
        print("Value not accepted (Please add Stealth using the edit function)")

    cunning = int(input(f"\nEnter {new_card}'s cunning value (1-25): "))
    if 1 < stealth < 25:
        deck[new_card]["Cunning"] = cunning
    else:
        print("Value not accepted (Please add Cunning using the edit function)")

    print(f"\nNew card {new_card} successfully added to the deck!")


# Edit card
def edit_card():
    existing_card = input("\nEnter the name of the card you want to edit: ").title()
    if existing_card in deck:

        # Allows user to edit existing card value or keep it the same (between 1 and 25)
        new_strength = int(input(f"\nEnter {existing_card}'s new strength value; 1-25 (0 to keep the same): "))
        if 1 < new_strength < 25:
            deck[existing_card]["Strength"] = new_strength
        else:
            print("Value not accepted")

        new_speed = int(input(f"\nEnter {existing_card}'s new speed value; 1-25 (0 to keep the same): "))
        if 1 < new_speed < 25:
            deck[existing_card]["Speed"] = new_speed
        else:
            print("Value not accepted")

        new_stealth = int(input(f"\nEnter {existing_card}'s new stealth value; 1-25 (0 to keep the same): "))
        if 1 < new_stealth < 25:
            deck[existing_card]["Stealth"] = new_stealth
        else:
            print("Value not accepted")

        new_cunning = int(input(f"\nEnter {existing_card}'s new cunning value; 1-25 (0 to keep the same): "))
        if 1 < new_cunning < 25:
            deck[existing_card]["Cunning"] = new_cunning
        else:
            print("Value not accepted")

        print(f"{existing_card} successfully updated!")

    else:
        print("This monster does not exist")


# Delete card
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
