# Monster Cards Final Version - 3/05/23


import easygui as gui


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
    print(deck_display)     # Not printing via gui because the text is too long to fit in a msgbox


# Add new card
def add_card():

    # Create new card name
    new_card = gui.enterbox("Enter the new monster name: ").title()
    if new_card in deck:
        gui.msgbox("That card already exists")
    else:
        deck[new_card] = {}

        # Adds the values for 4 variables: strength, speed, stealth and cunning between 1 and 25
        strength = gui.integerbox(f"Enter {new_card}'s strength value (1-25): ")
        if 0 < strength < 26:
            deck[new_card]["Strength"] = strength
        else:
            gui.msgbox("Value not accepted\n(Please add Strength later using the edit function)")

        speed = gui.integerbox(f"Enter {new_card}'s speed value (1-25): ")
        if 0 < speed < 26:
            deck[new_card]["Speed"] = speed
        else:
            gui.msgbox("Value not accepted\n(Please add Speed later using the edit function)")

        stealth = gui.integerbox(f"Enter {new_card}'s stealth value (1-25): ")
        if 0 < stealth < 26:
            deck[new_card]["Stealth"] = stealth
        else:
            gui.msgbox("Value not accepted\n(Please add Stealth later using the edit function)")

        cunning = gui.integerbox(f"Enter {new_card}'s cunning value (1-25): ")
        if 0 < stealth < 26:
            deck[new_card]["Cunning"] = cunning
        else:
            gui.msgbox("Value not accepted\n(Please add Cunning later using the edit function)")

        gui.msgbox(f"New card {new_card} successfully added to the deck!")


# Edit card
def edit_card():
    existing_card = gui.enterbox("Enter the name of the card you want to edit: ").title()
    if existing_card in deck:

        # Allows user to edit existing card value or keep it the same (between 1 and 25)
        new_strength = gui.integerbox(f"Enter {existing_card}'s new strength value; 1-25"
                                      f"\n(any other number to keep the same): ")
        if 0 < new_strength < 26:
            deck[existing_card]["Strength"] = new_strength
        else:
            gui.msgbox("Value not accepted, therefore skipped")

        new_speed = gui.integerbox(f"Enter {existing_card}'s new speed value; 1-25"
                                   f"\n(any other number to keep the same): ")
        if 0 < new_speed < 26:
            deck[existing_card]["Speed"] = new_speed
        else:
            gui.msgbox("Value not accepted, therefore skipped")

        new_stealth = gui.integerbox(f"Enter {existing_card}'s new stealth value; 1-25"
                                     f"\n(any other number to keep the same): ")
        if 0 < new_stealth < 26:
            deck[existing_card]["Stealth"] = new_stealth
        else:
            gui.msgbox("Value not accepted, therefore skipped")

        new_cunning = gui.integerbox(f"Enter {existing_card}'s new cunning value; 1-25"
                                     f"\n(any other number to keep the same): ")
        if 0 < new_cunning < 26:
            deck[existing_card]["Cunning"] = new_cunning
        else:
            gui.msgbox("Value not accepted, therefore skipped")

        gui.msgbox(f"{existing_card} successfully updated!")

    else:
        gui.msgbox("That card does not exist")


# Delete card
def del_card():
    existing_card = gui.enterbox("Enter the name of the card you want to delete: ").title()
    if existing_card in deck:
        deck.pop(existing_card)
        gui.msgbox(f"{existing_card} successfully removed from the deck!")
    else:
        gui.msgbox("That card does not exist")


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
    choice = gui.buttonbox("Please select an option", "Main Menu", choices=["Add card", "Edit card",
                                                                            "Delete card", "Print menu", "Exit"])

    if choice == "Add card":
        add_card()

    elif choice == "Edit card":
        edit_card()

    elif choice == "Delete card":
        del_card()

    elif choice == "Print menu":
        print_deck()

    elif choice == "Exit":
        gui.msgbox("*** Thank you for using this program ***")
        exit()
