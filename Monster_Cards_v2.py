# Monster Cards V2 - 1/05/23
# Adds a menu interface so the user can easily access each function

def print_deck():
    deck_display = ""
    deck_display += "-------------------------\n"
    deck_display += "*** Full Card Deck ***\n"

    for monster_id, monster_info in deck.items():
        deck_display += f"\nMonster name: {monster_id}"
        for key in monster_info:
            deck_display += f"\n{key}: {monster_info[key]}"
        deck_display += "\n"

    deck_display += "-------------------------"
    print(deck_display)


def add_card():
    print("add card")


def edit_card():
    print("edit card")


def del_card():
    print("delete card")


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
